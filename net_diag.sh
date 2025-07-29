#!/usr/bin/env bash
set -euo pipefail

LOGFILE="net_diag_$(date +'%Y%m%d_%H%M%S').log"
HOSTS_FILE="hosts.txt"

log() { echo "[$(date +'%H:%M:%S')] $*" | tee -a "$LOGFILE"; }

log "Starting network diagnostics"

# 1. Check interfaces
log "Interface status:"
ip -brief a | tee -a "$LOGFILE"

# 2. Ping each host
while read -r HOST; do
  log "Pinging $HOST..."
  if ping -c 3 -W 2 "$HOST" &> /dev/null; then
    log "SUCCESS: $HOST is reachable"
  else
    log "FAIL: $HOST is not reachable"
  fi
done < "$HOSTS_FILE"

# 3. Summary
log "Diagnostics complete. Log saved to $LOGFILE"