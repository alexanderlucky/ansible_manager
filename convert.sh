#!/usr/bin/env bash

ROLES_DIR="./roles"

has_content() {
    local file="$1"

    [ -f "$file" ] || return 1

    grep -q '[^[:space:]#]' "$file"
}

indent_file() {
    sed '/^---[[:space:]]*$/d' "$1" | sed 's/^/    /'
}

for role in "$ROLES_DIR"/*; do
    [ -d "$role" ] || continue

    role_name=$(basename "$role")
    output="${role_name}.yml"

    {
        echo "---"
        echo "- hosts: all"
        echo "  become: yes"
        echo

        if has_content "$role/vars/main.yml"; then
            echo "  vars:"
            indent_file "$role/vars/main.yml"
            echo

            if has_content "$role/defaults/main.yml"; then
                indent_file "$role/defaults/main.yml"
                echo
            fi
            
            echo

        fi

        if has_content "$role/tasks/main.yml"; then
            echo "  tasks:"
            indent_file "$role/tasks/main.yml"
            echo
        fi

        if has_content "$role/handlers/main.yml"; then
            echo "  handlers:"
            indent_file "$role/handlers/main.yml"
            echo
        fi

    } > "$output"

    echo "Created $output"
done