#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_kaboom_0.py                                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 14:35:38 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 14:43:15 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print(f"Testing record light spell: {alchemy.grimoire.light_spell_record('Fantasy', 'Earth, wind and fire')}")