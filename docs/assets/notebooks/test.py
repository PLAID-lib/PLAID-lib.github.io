import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import os

    from datasets import load_dataset
    from IPython.display import Image as IPyImage
    from IPython.display import display
    from PIL import Image as PILImage
    from plaid.bridges.huggingface_bridge import (
        huggingface_dataset_to_plaid,
        huggingface_description_to_problem_definition,
    )

    from plaid_ops.common.visualization import plot_field
    from plaid_ops.mesh.feature_engineering import (
        compute_sdf,
        update_dataset_with_sdf,
        update_sample_with_sdf,
    )

    hf_dataset = load_dataset(
        "PLAID-datasets/2D_Multiscale_Hyperelasticity", split="all_samples"
    )
    pb_def = huggingface_description_to_problem_definition(hf_dataset.info.description)
    ids = pb_def.get_split("DOE_train")[:2]
    dataset, _ = huggingface_dataset_to_plaid(hf_dataset, ids=ids, processes_number=2)
    return (
        IPyImage,
        PILImage,
        compute_sdf,
        dataset,
        display,
        ids,
        os,
        plot_field,
        update_dataset_with_sdf,
        update_sample_with_sdf,
    )


@app.cell
def _(dataset, ids, update_sample_with_sdf):
    sample = dataset[ids[0]]

    print("[before update] 'sdf' in sample fields ?", "sdf" in sample.get_field_names())
    updated_sample = update_sample_with_sdf(sample)
    print(
        "[after update] 'sdf' in sample fields ?", "sdf" in updated_sample.get_field_names()
    )
    return


@app.cell
def _(dataset, ids, update_dataset_with_sdf):
    print(
        "[before update] 'sdf' in dataset fields ?",
        "sdf" in dataset[ids[0]].get_field_names(),
    )
    updated_dataset = update_dataset_with_sdf(dataset)
    print(
        "[after update] 'sdf' in dataset fields ?",
        "sdf" in updated_dataset[ids[0]].get_field_names(),
    )
    return


@app.cell
def _(compute_sdf, dataset, ids):
    sample2 = dataset[ids[0]]
    computed_sdf = compute_sdf(sample2)
    return computed_sdf, sample2


@app.cell
def _(IPyImage, PILImage, computed_sdf, display, os, plot_field, sample2):
    img_name = "feature_engineering_1.png"
    if os.environ.get("READTHEDOCS") == "True" or os.environ.get("GITHUB_ACTIONS"):
        display(IPyImage(filename=img_name))
    else:
        img_array = plot_field(
            sample2,
            computed_sdf,
            title="SDF illustration",
            scalar_bar_args={"title": "sdf"},
        )
        img = PILImage.fromarray(img_array)
        img.save(img_name)
        display(img)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
