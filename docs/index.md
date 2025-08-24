# Physics-Learning AI Datamodel

<!-- <p style="text-align:center;">
  <img src="../assets/images/PLAID-large-logo.png" alt="logo" title="Logo" style="width:40%;"/>
</p> -->

## Introduction

### PLAID (Physics-Learning AI Datamodel): The Missing Layer for Scientific ML

Keep your simulation data intact, query it intuitively, and transform it seamlessly for deep learning.

PLAID is an open framework that makes it easy to represent and share datasets from complex physics simulations. It introduces a common standard for describing simulation data and comes with a library to create, explore, and manipulate complex datasets of physics similations. PLAID was first developed at SafranTech, the research and innovation center of [Safran Group](https://www.safran-group.com/).


### Why Another Data Model?

In machine learning, datasets are often treated as flat tables, sequences, or images. Standard frameworks — Hugging Face, PyTorch, TensorFlow — assume your data is already regular, homogeneous, and columnar. But in scientific and industrial applications, this assumption rarely holds:

- Simulations produce hierarchical, multi-zone data.
- Fields have heterogeneous shapes, types, and metadata.
- Implicit conventions vary from one simulation to another.

Traditional ML datasets are not designed to handle this complexity efficiently. Flattening, padding, or converting these structures into a standard tabular format can be error-prone, memory-intensive, and slow, and it often destroys critical information about the underlying physical structure.

PLAID fills this gap by sitting upstream in the ML pipeline, bridging raw scientific data and ML-ready formats:

1. Capture the full structure: PLAID preserves hierarchical, multi-field, multi-zone data, including metadata, defaults, and units.
2. Simplify access: Intuitive APIs let you query fields, arrays, and derived quantities without flattening or rewriting your trees.
3. Prepare for ML: When needed, PLAID can produce ML-ready datasets (PyTorch, PyG, or Hugging Face style), while keeping memory and computation efficient.

In short: PLAID is not “just another dataset format.” It is a scientific data management layer, designed for the complex, heterogeneous, high-dimensional world of physics-based simulations, where preparing your data for ML is as important as the model itself.

## Open source

The open source project is hosted on GitHub under the [PLAID-lib](https://github.com/PLAID-lib) organization. The project currently contains three librairies:

- [plaid](https://github.com/PLAID-lib/plaid) is the core library of the PLAID project.
- [plaid-bridges](https://github.com/PLAID-lib/plaid-bridges): provides integrations into machine learning frameworks such as PyTorch Geometric.
- [plaid-ops](https://github.com/PLAID-lib/plaid-bridges): a collection of standardized operations on PLAID samples and datasets.

## Paper

Check out the [PLAID preprint](https://arxiv.org/abs/2505.02974) recently submitted to arXiv!
