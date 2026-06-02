# PLAID — Physics Learning AI Data Model
**The missing data layer between physics simulations and scientific ML.**

PLAID is an open framework for representing, sharing, and learning from datasets of complex physics simulations. It defines a common standard for simulation data and ships a Python library to create, explore, store, and stream them.

## Why another data model?

Mainstream ML stacks (Hugging Face, PyTorch, TensorFlow) assume data is regular, homogeneous, and columnar. Real simulation data is not: it is **hierarchical and multi-zone**, with **heterogeneous fields, shapes, and metadata**, often governed by **implicit, solver-specific conventions**. Flattening or padding it into tabular form is error-prone, memory-hungry, and erases the physical structure the model should learn from.

## What PLAID provides

- **Fidelity** — Keep all the complexity of your simulation data — meshes, fields, tags, time, and
    multiphysics structure — and exploit it directly in ML pipelines.
- **Out-of-core datasets** — Datasets are accessed sample by sample, so full datasets do not need to be loaded
    into memory.
- **Parallel I/O** — `save_to_disk` can shard sample IDs across multiple processes for fast dataset
    generation and writing.
- **Multiple storage backends** — Use **CGNS**, **Hugging Face Datasets**, or **Zarr** through a unified API for
    local disk, Hub download, and streaming workflows.
- **Selective reading** — Request only the features you need and, when necessary, only selected indices within large variable arrays.
- **Interactive viewer** — Launch `plaid-viewer` to browse local or streamed datasets, inspect samples in 3D,
    select features, and visualize fields.
