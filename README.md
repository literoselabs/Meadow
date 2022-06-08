# Meadow
High-availability platform for financially reasonable (poor) people.

## Goals:
- Machine provisioning from Metal through netboot or local install (PXE and agents)
- Container orchestration (Kubernetes)
- Logging and metrics (CPU usage)
- Autoscaling (Based on container and host CPU usages)
- Load balancing (Floating IPs and passive-passive algorithms)
- High availability (Health checks)
- Storage services (block, object and secrets) with cold storage capabilities
- Hybrid cloud compatible (Running with GCP and AWS compute)
- Backups (…and ability to restore to/from Cloud)
- Authentication and Authorisation (RBAC and AD-capable)
- Hardware capabilities (certain amounts of CPU, RAM, Storage and GPU)
- Device passthrough (like easy USB device passthrough)
- Accepts any storage medium and any compute device (Heterogenous)
- Security (Encrypted nodes by allowing boot through Dropbear encryption unlock)
- Single instance recovery (like a DB running from a DRDB and another instance starting if that one fails and is killed)
- ML workloads (serving PyTorch and TF models from different nodes)?
- Networking abilities (automatic VPN between nodes)
- No Master and Worker nodes, although Voter nodes (like RPi) can be kept just to reach consensus
- Editing each node's '/etc/hosts' file as a pseudo-DNS server
- Temporary compute and storage nodes
- Ability to move data through and to a temporary node 
- Benchmarks hardware for capabilties
- Configurable replication options
- Good API
- Web and CLI interfaces

## Provisioning:
- Bootstrap new server using commandline interface configurator.
- Provision new servers by allowing boot from PXE or small local agent providing commandline access while signalling host to bootstrap (service discovery)

## Technologies:
- Flask?
- ZFS on DRDB (bit-rot and replication protected)
- Kubernetes (K3s)
- Minio
- Written in Python 3.8 for compatibility
- Runs on Ubuntu
- SSH for commands
- PySyncObj for distributed objects
- '/etc/hosts' editing for pseudo-DNS

## Prerequisites:
- Python 3 as an absolute minimum
- Bootstrap host should have prerequiste packages listed in 'data/packages.json' installed but it will attempt to install those at best-effort (may fail) only.
- Hosts without PXE support require absolute minimum and manual launch of agent.
- Hosts supporting PXE 

## Usage
1. Run the following command for usage guidance after acquiring project files:
```python3 meadow.py```