import cdd
V = [[1.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0],
     [1.0, -4.0, -40.0, 4.0, 28.22314601, -4.83120097, -20.08886368],
     [1.0, -4.0, -40.0, -4.0, 30.19098601, -1.01021223, -20.08886368],
     [1.0, 4.0, -40.0, 4.0, 28.22314601, 1.01021223, -18.12102368],
     [1.0, 4.0, -40.0, -4.0, 30.19098601, 4.83120097, -18.12102368],
     [1.0, -4.0, -40.0, 4.0, 28.0999032, -4.88536345, -20.75373128],
     [1.0, -4.0, -40.0, -4.0, 30.0677432, -0.93140119, -20.75373128],
     [1.0, 4.0, -40.0, 4.0, 28.0999032, 0.93140119, -18.78589128],
     [1.0, 4.0, -40.0, -4.0, 30.0677432, 4.88536345, -18.78589128],
     [1.0, -4.0, -40.0, 4.0, 29.05601375, -5.00096, -20.95358629],
     [1.0, -4.0, -40.0, -4.0, 31.02398625, -1.00704, -20.95358629],
     [1.0, 4.0, -40.0, 4.0, 29.05601375, 1.00704, -18.98561378],
     [1.0, 4.0, -40.0, -4.0, 31.02398625, 5.00096, -18.98561378],
     [1.0, -4.0, -40.0, 4.0, 29.05601375, -4.91296, -20.07358622],
     [1.0, -4.0, -40.0, -4.0, 31.02398625, -1.09504, -20.07358622],
     [1.0, 4.0, -40.0, 4.0, 29.05601375, 1.09504, -18.10561371],
     [1.0, 4.0, -40.0, -4.0, 31.02398625, 4.91296, -18.10561371],
     [1.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0],
     [1.0, -4.0, 40.0, -4.0, -28.02714601, -1.01021223, 17.92502368],
     [1.0, -4.0, 40.0, 4.0, -30.38698601, -4.83120097, 17.92502368],
     [1.0, 4.0, 40.0, -4.0, -28.02714601, 4.83120097, 20.28486368],
     [1.0, 4.0, 40.0, 4.0, -30.38698601, 1.01021223, 20.28486368],
     [1.0, -4.0, 40.0, 4.0, -30.2637432, -4.88536345, 18.58989128],
     [1.0, -4.0, 40.0, -4.0, -27.9039032, -0.93140119, 18.58989128],
     [1.0, 4.0, 40.0, -4.0, -27.9039032, 4.88536345, 20.94973128],
     [1.0, 4.0, 40.0, 4.0, -30.2637432, 0.93140119, 20.94973128],
     [1.0, -4.0, 40.0, 4.0, -31.21985375, -5.00096, 18.78974629],
     [1.0, -4.0, 40.0, -4.0, -28.86014625, -1.00704, 18.78974629],
     [1.0, 4.0, 40.0, -4.0, -28.86014625, 5.00096, 21.14945378],
     [1.0, 4.0, 40.0, 4.0, -31.21985375, 1.00704, 21.14945378],
     [1.0, -4.0, 40.0, 4.0, -31.21985375, -4.91296, 17.90974622],
     [1.0, -4.0, 40.0, -4.0, -28.86014625, -1.09504, 17.90974622],
     [1.0, 4.0, 40.0, -4.0, -28.86014625, 4.91296, 20.26945371],
     [1.0, 4.0, 40.0, 4.0, -31.21985375, 1.09504, 20.26945371]]
V_cdd = cdd.Matrix(V, number_type = 'float')
V_cdd.rep_type = cdd.RepType.GENERATOR
P = cdd.Polyhedron(V_cdd)
