#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_spellbook.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 13:42:09 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 14:47:50 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def light_spell_allowed_ingredients() -> list[str] :
    allowed_ingredients: list[str] = ["earth", "air", "fire", "water"]
    return (allowed_ingredients)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return (f"Spell recorded: {spell_name} ({result})")
    else:
        return (f"Spell rejected: {spell_name} ({result})")
