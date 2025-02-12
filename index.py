import marimo

__generated_with = "0.11.0"
app = marimo.App(width="full", app_title="Index")


@app.cell
def _(mo):
    mo.md(r"""# Hello""")
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import os
    return mo, os, pd


@app.cell(hide_code=True)
def _(mo, notebooks_dict):
    mo.sidebar(
        [
            mo.md("# Marimo Extra"),
            mo.nav_menu(
                {
                    "/index.html": f"{mo.icon('lucide:home')} Home",
                    f"{mo.icon('lucide:book')} Notebooks": notebooks_dict,
                    "#about": f"{mo.icon('lucide:user')} About",
                },
                orientation="vertical",
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _():
    import marimo_extra as me
    return (me,)


@app.cell(hide_code=True)
def _():
    # card = [
    #     me.ui.card(name="Gallary" , thumbnail=None, content="Tag: ML, Python", link="/notebooks/fibonacci.py"),
    #     me.ui.card(name="Gallary" , thumbnail=None, content="Tag: ML, Python", link="/notebooks/fibonacci.py"),

    #     me.ui.card(name="Gallary" , thumbnail=None, content="Tag: ML, Python", link="/notebooks/fibonacci.py"),
    #     me.ui.card(name="Gallary" , thumbnail=None, content="Tag: ML, Python", link="/notebooks/fibonacci.py")]
    # for c in card:
    #     mo.output.append(c)
    return


@app.cell
def _():
    return


@app.cell
def _(me, os, pd):
    notebooks = pd.read_csv(os.path.join('public', 'index.csv'))
    notebooks
    me.ui.gallery(data = notebooks)
    return (notebooks,)


@app.cell
def _(mo, notebooks, os):

    names = notebooks['Name'].values
    # paths = '/'+notebooks['Path'].values
    base = os.path.basename(str(mo.notebook_dir()))
    paths =  '/'+base+'/'+notebooks['Path'].values
    notebooks_dict = dict(zip(paths, names))
    notebooks_dict
    return base, names, notebooks_dict, paths


@app.cell
def _():
    # for notebook in notebooks:
    #     print("Name: " , notebook[0], "Link: ", notebook[1], "Types: ", notebook[2], "Thumbnail: ", notebook[3], "Tags: ", notebook[4])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
