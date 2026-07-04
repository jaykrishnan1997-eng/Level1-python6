#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_5.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 11:22:26 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 11:33:51 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air

if __name__ == "__main__":
    print("=== Alembic 5 ===")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")
