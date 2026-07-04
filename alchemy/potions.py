#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   potions.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 11:35:22 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 12:04:19 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import elements as root_elements
from . import elements as local_elements


def healing_potion() -> str:
    earth = local_elements.create_earth()
    air = local_elements.create_air()
    return (f"Healing potion brewed with ’{earth}’ and ’{air}'")


def strength_potion() -> str:
    fire = root_elements.create_fire()
    water = root_elements.create_water()
    return (f"Strength potion brewed with ’{fire}’ and ’{water}'")
