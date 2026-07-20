#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 12:37:32 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/20 10:07:53 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation.recipes

if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print(
        f"Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}"
    )
