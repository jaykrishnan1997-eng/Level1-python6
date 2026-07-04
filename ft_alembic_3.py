#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 10:33:54 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 10:45:37 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy.elements import create_air

if __name__ == "__main__":
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py "
          "using 'from ... import ...' structure")
    print("Testing create_air: " + create_air() + "\n")
