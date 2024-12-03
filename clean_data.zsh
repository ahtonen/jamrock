#!/bin/zsh

for file in data/*.csv; do
  if [[ -f "$file" ]]; then
    new_name=$(echo "$file" | sed 's/[[:space:]]*.csv$/.csv/' | tr ' ' '_')
    
    if [[ "$file" != "$new_name" ]]; then
      mv "$file" "$new_name"
      echo "Renamed: $file -> $new_name"
    fi
  fi
done