# Collections of Scripts to Automate Jobs in AWS

```bash
pip3 install -r requirements.txt
```

# AUTOMATE SNAPSHOTS

## RDS Snapshot

```bash
#shorter version
python3 snapshot_db/rds/snapshot_rds.py -db database-1,database-2 -r us-east-1
#longer version
python3 snapshot_db/rds/snapshot_rds.py --db_instances database-1,database-2 --region us-east-1
```

## RDS Aurora Snapshot

```bash
#shorter version
python3 snapshot_db/rds_aurora/snapshot_auroradb.py -c database-1,database-2 -r us-east-1
#longer version
python3 snapshot_db/rds_aurora/snapshot_auroradb.py --cluster database-1,database-2 --region us-east-1
```

# INSTANCE SCHEDULER

## Update Schedule of Instances
```bash
bash instance-scheduler/update_scheduler.sh customer-1,customer-2,customer-3 00:00 23:59
```