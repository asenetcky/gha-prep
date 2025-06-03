import polars as pl

df = DataFrame({
    "a" = [1,2,3,4,5],
    "b" = [5,6,4,7,3],
    "c" = ["a","b","c","f","k"]
    "pools" = [1.0,2.2,3.4,7.8,99.9]
})


filtered=(
    df
    .filter(pl.col("a") > 2)
    .with_columns(d=pl.col("a") * pl.col("b"))
)

print(filtered.head())
