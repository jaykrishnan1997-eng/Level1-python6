#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_2.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 10:30:38 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 10:45:32 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.elements

if __name__ == "__main__":
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth: " + alchemy.elements.create_earth() + "\n")
