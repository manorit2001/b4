#!/bin/bash
set -xe
tail -n +2 .git/filter-repo/commit-map | xargs -I {} bash -c "echo \"copying notes from {}\"; git notes copy --force {}"
