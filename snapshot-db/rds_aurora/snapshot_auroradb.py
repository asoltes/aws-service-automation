import boto3
import time
import argparse
import concurrent.futures
import sys

def current_time():
    # Returns the current time as a formatted string
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

def create_rds_snapshots(cluster_names, region):
    # Creates RDS snapshots for the given cluster names in the specified region
    rds = boto3.client('rds', region_name=region)
    futures = []

    # Execute snapshot creation concurrently for all cluster names
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(cluster_names)) as executor:
        for cluster_name in cluster_names:
            snapshot_id = f'{cluster_name}-snapshot-{current_time()}'
            future = executor.submit(rds.create_db_cluster_snapshot,
                                     DBClusterIdentifier=cluster_name,
                                     DBClusterSnapshotIdentifier=snapshot_id)
            futures.append(future)
            print(f"Snapshot creation started for {cluster_name}: {snapshot_id}")

    snapshots_available = False
    while not snapshots_available:
        snapshots_available = True
        time.sleep(30)
        # Check the status of each snapshot creation
        for future in futures:
            if future.done() and not future.cancelled():
                try:
                    response = future.result()
                    snapshot_id = response['DBClusterSnapshot']['DBClusterSnapshotIdentifier']
                    snapshot_response = rds.describe_db_cluster_snapshots(DBClusterSnapshotIdentifier=snapshot_id)
                    snapshot_status = snapshot_response['DBClusterSnapshots'][0]['Status']

                    # Check if the snapshot is still being created or is available
                    if snapshot_status != 'available':
                        snapshots_available = False
                        print(f"Snapshot {snapshot_id} is still being created")
                    else:
                        print(f"Snapshot {snapshot_id} is now available")
                except Exception as e:
                    print(f"Error occurred while creating snapshot: {e}")
                    sys.exit(1)

def parse_arguments():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Create RDS snapshots')
    parser.add_argument('-c', '--cluster', metavar='aurora-db-clusters', type=str,
                        help='a comma-separated list of RDS cluster names')
    parser.add_argument('-r', '--region', metavar='region', type=str, help='specify the rds region')
    return parser.parse_args()

def main():
    args = parse_arguments()
    cluster_names = [name.strip() for name in args.cluster.split(',')]
    create_rds_snapshots(cluster_names, args.region)

if __name__ == '__main__':
    main()
