def validate_target_column(df, target):
    if target not in df.columns:
        raise ValueError("Target column not found in CSV")
