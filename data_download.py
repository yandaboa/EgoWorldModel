from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="builddotai/Egocentric-10K",
    repo_type="dataset",
    local_dir="/mnt/storage/egocentric10k_factory51",
    allow_patterns=[
        "factory_051/**",          # pick a factory
        "**/intrinsics.json",      # keep intrinsics
        # or narrow further to a worker/shard:
        # "factory_051/workers/worker_001/*.tar",
    ],
)