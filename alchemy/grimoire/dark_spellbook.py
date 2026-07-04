#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_spellbook.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 14:31:50 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 14:35:21 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str] :
    allowed_ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return (allowed_ingredients)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return (f"Spell recorded: {spell_name} ({result})")
    else:
        return (f"Spell rejected: {spell_name} ({result})")
