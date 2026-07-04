#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 13:45:22 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 14:48:34 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed_ingredients = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(item in lowered for item in allowed_ingredients):
        return (f"{ingredients} - VALID")
    else:
        return (f"{ingredients} - INVALID")
