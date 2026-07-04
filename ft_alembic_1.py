#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_1.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 10:23:52 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 10:45:24 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from elements import create_water

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    print("Using: 'from ... import ...' structure to access elements.py")
    print("Testing create_water: " + create_water() + "\n")
