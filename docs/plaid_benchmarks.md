<img src="../assets/images/plaid_benchmarks.png" class="align-center" width="60%"
alt="PLAID Benchmarks" />

We provide interactive benchmarks hosted on Hugging Face, in which
anyone can test their own SciML method. These benchmarks involve
regression problems posed on datasets provided in PLAID format. Some of
these datasets have been introduced in the MMGP (Mesh Morphing Gaussian
Process) paper @casenave2023mmgp, and the PLAID paper
@casenave2025plaid. A ranking is automatically updated based on a score
computed on the testing set of each dataset. For the benchmarks to be
meaningful, the outputs on the testing sets are not made public.

The relative RMSE is the considered metric for comparing methods. Let
$\{ \mathbf{U}^i_{\rm ref} \}_{i=1}^{n_\star}$ and
$\{ \mathbf{U}^i_{\rm pred} \}_{i=1}^{n_\star}$ be the test observations
and predictions, respectively, of a given field of interest. The
relative RMSE is defined as

$$
\mathrm{RRMSE}_f(\mathbf{U}_{\rm ref}, \mathbf{U}_{\rm pred}) = \left( \frac{1}{n_\star}\sum_{i=1}^{n_\star} \frac{\frac{1}{N^i}\|\mathbf{U}^i_{\rm ref} - \mathbf{U}^i_{\rm pred}\|_2^2}{\|\mathbf{U}^i_{\rm ref}\|_\infty^2} \right)^{1/2},
$$

where $N^i$ is the number of nodes in the mesh $i$, and
$\max(\mathbf{U}^i_{\rm ref})$ is the maximum entry in the vector
$\mathbf{U}^i_{\rm ref}$. Similarly for scalar outputs:

$$
\mathrm{RRMSE}_s(\mathbf{w}_{\rm ref}, \mathbf{w}_{\rm pred}) = \left( \frac{1}{n_\star} \sum_{i=1}^{n_\star} \frac{|w^i_{\rm ref} - w_{\rm pred}^i|^2}{|w^i_{\rm ref}|^2} \right)^{1/2}.
$$

## Resources

<table style="width:99%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 52%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Dataset</p>
</blockquote></th>
<th><blockquote>
<p>Benchmark</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Tensile2d</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/Tensile2d"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="Tensile2d_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.14840177"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.14840177.svg"
alt="Tensile2d_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/Tensile2dBenchmark"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="Tensile2d_Be" /></a></td>
</tr>
<tr class="even">
<td><strong>2D_MultiScHypEl</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/2D_Multiscale_Hyperelasticity"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="2D_MultiScHypEl_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.14840446"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.14840446.svg"
alt="2D_MultiScHypEl_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/2DMultiscaleHyperelasticityBenchmark"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="2D_MultiScHypEl_Be" /></a></td>
</tr>
<tr class="odd">
<td><strong>2D_ElPlDynamics</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/2D_ElastoPlastoDynamics"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="2D_ElPlDynamics_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.15286369"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.15286369.svg"
alt="2D_ElPlDynamics_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/2DElastoPlastoDynamics"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="2D_ElPlDynamics_Be" /></a></td>
</tr>
<tr class="even">
<td><strong>Rotor37</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/Rotor37"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="Rotor37_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.14840190"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.14840190.svg"
alt="Rotor37_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/Rotor37Benchmark"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="Rotor37_Be" /></a></td>
</tr>
<tr class="odd">
<td><strong>2D_profile</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/2D_profile"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="2D_profile_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.15155119"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.15155119.svg"
alt="2D_profile_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/2DprofileBenchmark"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="2D_profile_Be" /></a></td>
</tr>
<tr class="even">
<td><strong>VKI-LS59</strong></td>
<td><a
href="https://huggingface.co/datasets/PLAID-datasets/VKI-LS59"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg"
alt="VKI-LS59_HF" /></a> <a
href="https://doi.org/10.5281/zenodo.14840512"><img
src="https://zenodo.org/badge/DOI/10.5281/zenodo.14840512.svg"
alt="VKI-LS59_Z" /></a></td>
<td><a
href="https://huggingface.co/spaces/PLAIDcompetitions/VKILS59Benchmark"><img
src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg"
alt="VKI-LS59_Be" /></a></td>
</tr>
</tbody>
</table>

AirfRANS, introduced in `airfrans` is an additional dataset provided in
PLAID format and various variants. Since the outputs on the testing sets
are public, no benchmark application is provided for this dataset.

|                       |                                                                                                                                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AirfRANS original** | [![AirfRANS_O_HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg)](https://huggingface.co/datasets/PLAID-datasets/AirfRANS_original) [![AirfRANS_O_Z](https://zenodo.org/badge/DOI/10.5281/zenodo.14840387.svg)](https://doi.org/10.5281/zenodo.14840387) |
| **AirfRANS clipped**  | [![AirfRANS_C_HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg)](https://huggingface.co/datasets/PLAID-datasets/AirfRANS_clipped) [![AirfRANS_C_Z](https://zenodo.org/badge/DOI/10.5281/zenodo.14840377.svg)](https://doi.org/10.5281/zenodo.14840377)  |
| **AirfRANS remeshed** | [![AirfRANS_R_HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/dataset-on-hf-md-dark.svg)](https://huggingface.co/datasets/PLAID-datasets/AirfRANS_remeshed) [![AirfRANS_R_Z](https://zenodo.org/badge/DOI/10.5281/zenodo.14840388.svg)](https://doi.org/10.5281/zenodo.14840388) |

## Benchmark results

As of August 5, 2025

| Dataset                                        | MGN    | MMGP   | Vi-Transf. | Augur  | FNO    | MARIO  |
|------------------------------------------------|--------|--------|------------|--------|--------|--------|
| <span class="title-ref">Tensile2d</span>       | 0.0673 | 0.0026 | 0.0116     | 0.0154 | 0.0123 | 0.0038 |
| <span class="title-ref">2D_MultiScHypEl</span> | 0.0437 | ❌     | 0.0325     | 0.0232 | 0.0302 | 0.0573 |
| <span class="title-ref">2D_ElPlDynamics</span> | 0.1202 | ❌     | 0.0227     | 0.0346 | 0.0215 | 0.0319 |
| <span class="title-ref">Rotor37</span>         | 0.0074 | 0.0014 | 0.0029     | 0.0033 | 0.0313 | 0.0017 |
| <span class="title-ref">2D_profile</span>      | 0.0593 | 0.0365 | 0.0312     | 0.0425 | 0.0972 | 0.0307 |
| <span class="title-ref">VKI-LS59</span>        | 0.0684 | 0.0312 | 0.0193     | 0.0267 | 0.0215 | 0.0124 |

❌: Not compatible with topology variation

<div class="note">

<div class="title">

Note

</div>

- MMGP does not support variable mesh topologies, which limits its
  applicability to certain datasets and often necessitates custom
  preprocessing for new cases. However, when morphing is either
  unnecessary or inexpensive, it offers a highly efficient solution,
  combining fast training with good accuracy (e.g., `Tensile2d` and
  `Rotor37`).
- MARIO is computationally expensive to train but achieves consistently
  a very strong performance across most datasets. Its result on
  `2D_MultiScHypEl` is slightly worse than other tested methods, which
  may reflect the challenge of capturing complex shape variability in
  these cases.
- Vi-Transformer and Augur perform well across all datasets, showing
  strong versatility and generalization capabilities.
- FNO suffers on datasets featuring unstructured meshes with pronounced
  anisotropies, due to the loss of accuracy introduced by projections to
  and from regular grids (e.g., `Rotor37` and `2D_profile`).
  Additionally, the use of a 3D regular grid on `Rotor37` results in
  substantial computational overhead.

</div>

## References
```bibtex