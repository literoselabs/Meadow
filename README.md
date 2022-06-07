# Meadow
High-availability platform for poor and reasonable people.

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
- Benchmarks hardware for capabilties
- Configurable replication options
- Good API
- Web and CLI interfaces

## Technologies:
- Flask?
- ZFS on DRDB (bit-rot and replication protected)
- Kubernetes (K3s)
- Minio
- Written in Python 3.8 for compatibility
- Runs on Ubuntu
- SSH for commands