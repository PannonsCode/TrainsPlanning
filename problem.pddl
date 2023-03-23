(define (problem train-problem)

	(:domain train-domain)

	(:objects T1 T2 T3 T4 T5 T6 A B C D E F G A_1 R_1 B_1 B_2 R_2 R_3 R_4 C_1 C_2 R_5 R_6 D_1 R_7 R_8 R_9 G_1 G_2 R_10 R_11 E_1 R_12 R_13 E_2 R_14 F_1 R_15 R_16 F_2 A_2 A_3 )

	(:init (train T1)(train T2)(train T3)(train T4)(train T5)(train T6)
		(station A)(station B)(station C)(station D)(station E)(station F)(station G)
		(railway A_1)(railway R_1)(railway B_1)(railway B_2)(railway R_2)(railway R_3)(railway R_4)(railway C_1)(railway C_2)(railway R_5)(railway R_6)(railway D_1)(railway R_7)(railway R_8)(railway R_9)(railway G_1)(railway G_2)(railway R_10)(railway R_11)(railway E_1)(railway R_12)(railway R_13)(railway E_2)(railway R_14)(railway F_1)(railway R_15)(railway R_16)(railway F_2)(railway A_2)(railway A_3)
		(isin A_1 A)(isin A_2 A)(isin A_3 A)(isin B_1 B)(isin B_2 B)(isin C_1 C)(isin C_2 C)(isin D_1 D)(isin E_1 E)(isin E_2 E)(isin F_1 F)(isin F_2 F)(isin G_1 G)(isin G_2 G)
		(conn A_1 R_1)(conn R_1 A_1)(conn R_1 B_1)(conn B_1 R_1)
		(conn R_1 B_2)(conn B_2 R_1)
		(conn R_1 R_2)(conn R_2 R_1)(conn R_2 R_3)(conn R_3 R_2)(conn R_3 R_4)(conn R_4 R_3)(conn R_4 C_1)(conn C_1 R_4)
		(conn R_4 C_2)(conn C_2 R_4)
		(conn R_3 R_5)(conn R_5 R_3)(conn R_5 R_6)(conn R_6 R_5)(conn R_6 D_1)(conn D_1 R_6)
		(conn R_5 R_7)(conn R_7 R_5)(conn R_7 R_8)(conn R_8 R_7)(conn R_8 D_1)(conn D_1 R_8)
		(conn R_7 R_9)(conn R_9 R_7)(conn R_9 G_1)(conn G_1 R_9)
		(conn R_9 G_2)(conn G_2 R_9)
		(conn R_2 R_10)(conn R_10 R_2)(conn R_10 R_11)(conn R_11 R_10)(conn R_11 E_1)(conn E_1 R_11)
		(conn R_10 R_12)(conn R_12 R_10)(conn R_12 R_13)(conn R_13 R_12)(conn R_13 E_2)(conn E_2 R_13)
		(conn R_12 R_14)(conn R_14 R_12)(conn R_14 F_1)(conn F_1 R_14)
		(conn R_11 R_15)(conn R_15 R_11)(conn R_15 R_16)(conn R_16 R_15)(conn R_16 F_2)(conn F_2 R_16)
		
		(conn A_3 R_15)(conn R_15 A_3)(conn R_15 E_1)(conn E_1 R_15)
		(conn R_11 R_12)(conn R_12 R_11)
		
		(conn R_2 B_1)(conn B_1 R_2)
		(conn R_2 B_2)(conn B_2 R_2)
		(conn R_10 R_3)(conn R_3 R_10)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		(conn R_4 R_5)(conn R_5 R_4)
		
		
		
		
		
		
		
		
		
		
		(conn R_6 R_7)(conn R_7 R_6)
		
		(conn R_8 R_9)(conn R_9 R_8)
		
		
		
		
		
		(conn R_6 R_8)(conn R_8 R_6)
		
		(conn R_13 R_14)(conn R_14 R_13)
		
		
		
		
		
		
		
		
		
		
		
		
		(at T1 A)(at T1 A_1)
		(instation T1)
		(at T2 B)(at T2 B_2)
		(instation T2)
		(at T3 C)(at T3 C_1)
		(instation T3)
		(at T4 D)(at T4 D_1)
		(instation T4)
		(at T5 F)(at T5 F_2)
		(instation T5)
		(at T6 R_7)
		(free R_1)(free B_1)(free R_2)(free R_3)(free R_4)(free C_2)(free R_5)(free R_6)(free R_8)(free R_9)(free G_1)(free G_2)(free R_10)(free R_11)(free E_1)(free R_12)(free R_13)(free E_2)(free R_14)(free F_1)(free R_15)(free R_16)(free A_2)(free A_3)
	)

	(:goal (and (at T1 E)(instation T1)(at T2 F)(instation T2)(at T4 A)(instation T4)(at T5 B)(instation T5)(at T6 C)(instation T6)(at T3 R_8)) ) 
)