# Collections of Scripts to Automate Jobs in AWS

```bash
pip3 install -r requirements.txt
```

# AUTOMATE SNAPSHOTS

## RDS Snapshot
shorter version
```bash
python3 snapshot_db/rds/snapshot_rds.py -db database-1,database-2 -r us-east-1

```
longer version
```bash
python3 snapshot_db/rds/snapshot_rds.py --db_instances database-1,database-2 --region us-east-1
```
## RDS Aurora Snapshot
shorter version
```bash
python3 snapshot_db/rds_aurora/snapshot_auroradb.py -c database-1,database-2 -r us-east-1
```

longer version
```bash
python3 snapshot_db/rds_aurora/snapshot_auroradb.py --cluster database-1,database-2 --region us-east-1
```
# Instance Scheduler 

## Update Schedule of Instances
```bash
bash update_scheduler.sh barclays,db,ets,goldensource,jefferies,jpm,ubs 00:00 23:59
```