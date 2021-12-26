def tower_builder(n_floors):
    # build here
        len = n_floors * 2 - 1
        def_str = ""
        result = []
        for i in range(0, len):
                def_str += "*"
        result.append(def_str)
        for i in range(1, n_floors):
                def_str = ""
                len_temp = (n_floors-i) * 2 - 1
                for i in range(0, len_temp):
                        def_str += "*"
                result.append(def_str.center(len))
        result = result[::-1]
        return result
