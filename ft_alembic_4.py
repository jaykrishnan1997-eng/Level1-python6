#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/04 10:45:56 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/04 11:21:56 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

if __name__ == "__main__":
    print("Accessing the alchemy module using 'import alchemy'")
    print("Testing create_air: " + alchemy.create_air())
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth:")
    try:
        print(f"{alchemy.create_earth()}")
    except AttributeError as e:
        print(f"{e}")
