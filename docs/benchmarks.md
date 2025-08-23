# PLAID Benchmarks

<div style="text-align:center;">
<img src="../assets/images/plaid_benchmarks.png" class="align-center" width="60%"
alt="PLAID Benchmarks" />
</div>


We provide interactive benchmarks hosted on Hugging Face, in which
anyone can test their own SciML method. These benchmarks involve
regression problems posed on datasets provided in PLAID format. Some of
these datasets have been introduced in the MMGP (Mesh Morphing Gaussian
Process) paper [@casenave2023mmgp], and the PLAID paper
[@casenave2025plaid]. A ranking is automatically updated based on a score
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

## Interactive benchmark applications


<div class="grid cards">

  <div class="card">
    <p><strong>Tensile2d</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/Tensile2dBenchmark"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="Tensile2d_Be" style="height:30px;"/></a>
    </div>
  </div>

  <div class="card">
    <p><strong>2D_MultiScHypEl</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/2DMultiscaleHyperelasticityBenchmark"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="2D_MultiScHypEl_Be" style="height:30px;"/></a>
    </div>
  </div>

  <div class="card">
    <p><strong>2D_ElPlDynamics</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/2DElastoPlastoDynamics"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="2D_ElPlDynamics_Be" style="height:30px;"/></a>
    </div>
  </div>

  <div class="card">
    <p><strong>Rotor37</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/Rotor37Benchmark"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="Rotor37_Be" style="height:30px;"/></a>
    </div>
  </div>

  <div class="card">
    <p><strong>2D_profile</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/2DprofileBenchmark"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="2D_profile_Be" style="height:30px;"/></a>
    </div>
  </div>

  <div class="card">
    <p><strong>KI-LS59</strong></p>
    <div class="card-badges">
    <a href="https://huggingface.co/spaces/PLAIDcompetitions/VKILS59Benchmark"><img src="https://huggingface.co/datasets/huggingface/badges/resolve/main/open-in-hf-spaces-sm-dark.svg" alt="VKI-LS59_Be" style="height:30px;"/></a>
    </div>
  </div>

</div>



## Benchmark results

As of August 5, 2025

| <div style="text-align:center;"><p>Benchmark<p></div> | <div style="text-align:center;"><p>MGN<p></div>    | <div style="text-align:center;"><p>MMGP<p></div>   | <div style="text-align:center;"><p>Vi-Transf.<p></div> | <div style="text-align:center;"><p>Augur<p></div>  | <div style="text-align:center;"><p>FNO<p></div>    | <div style="text-align:center;"><p>MARIO<p></div>  |
|------------------------------------------------|--------|--------|------------|--------|--------|--------|
| <span class="title-ref">Tensile2d</span>       | 0.0673  |  **0.0026**  |   0.0116     |  0.0154   |  0.0123  |  *0.0038*  |
| <span class="title-ref">2D_MultiScHypEl</span> | 0.0437  |  ❌  |   0.0325     |  **0.0232**   |   *0.0302*  |  0.0573  |
| <span class="title-ref">2D_ElPlDynamics</span> | 0.1202  |  ❌  |   *0.0227*     |  0.0346    |  **0.0215**  |  0.0319  |
| <span class="title-ref">Rotor37</span>         | 0.0074  |  **0.0014**  |   0.0029     |  0.0033   |   0.0313  |  *0.0017*  |
| <span class="title-ref">2D_profile</span>      | 0.0593  |  0.0365  |   *0.0312*     |  0.0425   |  0.0972  |  **0.0307**  |
| <span class="title-ref">VKI-LS59</span>        | 0.0684  |  0.0312  |   *0.0193*     |  0.0267    |   0.0215  |  **0.0124**  |

❌: Not compatible with topology variation


!!! note
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


## References
\bibliography