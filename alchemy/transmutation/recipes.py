#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 12:23:39 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/20 10:07:06 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import elements as root_elements
from .. import elements as local_elements
from .. import potions


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew"
        f"’{local_elements.create_air()}’ and"
        f"’{potions.strength_potion()}’ mixed "
        f"with ’{root_elements.create_fire()}’"
    )
