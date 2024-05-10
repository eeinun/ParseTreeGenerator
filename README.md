# ParseTreeGenerator
working...

From this
```c
int facto(int n)
{
    return n * facto(n - 1);
}
```

To this
```mermaid
    flowchart BT
    node2_0(["Starting"])
    node7_14(["INT"])
    node12_34(["type_specifier"])
    node19_32(["declaration_specifiers"])
    node23_51(["IDENTIFIER"])
    node28_58(["direct_declarator"])
    node33_131(["'('"])
    node38_14(["INT"])
    node43_34(["type_specifier"])
    node50_229(["declaration_specifiers"])
    node54_51(["IDENTIFIER"])
    node59_58(["direct_declarator"])
    node66_332(["declarator"])
    node72_232(["parameter_declaration"])
    node77_231(["parameter_list"])
    node83_230(["parameter_type_list"])
    node87_335(["')'"])
    node95_58(["direct_declarator"])
    node102_57(["declarator"])
    node106_125(["'{'"])
    node111_208(["RETURN"])
    node116_74(["IDENTIFIER"])
    node121_92(["primary_expression"])
    node126_96(["postfix_expression"])
    node133_150(["unary_expression"])
    node139_99(["cast_expression"])
    node144_100(["multiplicative_expression"])
    node148_162(["'*'"])
    node153_74(["IDENTIFIER"])
    node158_92(["primary_expression"])
    node163_96(["postfix_expression"])
    node168_158(["'('"])
    node173_74(["IDENTIFIER"])
    node178_92(["primary_expression"])
    node183_96(["postfix_expression"])
    node190_150(["unary_expression"])
    node196_99(["cast_expression"])
    node201_100(["multiplicative_expression"])
    node207_101(["additive_expression"])
    node211_166(["'-'"])
    node216_75(["I_CONSTANT"])
    node221_93(["constant"])
    node226_92(["primary_expression"])
    node231_96(["postfix_expression"])
    node238_97(["unary_expression"])
    node243_99(["cast_expression"])
    node248_281(["multiplicative_expression"])
    node256_101(["additive_expression"])
    node262_102(["shift_expression"])
    node268_103(["relational_expression"])
    node274_104(["equality_expression"])
    node280_105(["and_expression"])
    node286_106(["exclusive_or_expression"])
    node292_107(["inclusive_or_expression"])
    node298_108(["logical_and_expression"])
    node304_109(["logical_or_expression"])
    node310_151(["conditional_expression"])
    node315_274(["assignment_expression"])
    node320_273(["argument_expression_list"])
    node324_361(["')'"])
    node332_96(["postfix_expression"])
    node339_97(["unary_expression"])
    node344_277(["cast_expression"])
    node351_100(["multiplicative_expression"])
    node357_101(["additive_expression"])
    node363_102(["shift_expression"])
    node369_103(["relational_expression"])
    node375_104(["equality_expression"])
    node381_105(["and_expression"])
    node387_106(["exclusive_or_expression"])
    node393_107(["inclusive_or_expression"])
    node399_108(["logical_and_expression"])
    node405_109(["logical_or_expression"])
    node411_151(["conditional_expression"])
    node416_152(["assignment_expression"])
    node421_320(["expression"])
    node425_392(["';'"])
    node432_221(["jump_statement"])
    node437_213(["statement"])
    node442_217(["block_item"])
    node447_216(["block_item_list"])
    node452_322(["'}'"])
    node459_129(["compound_statement"])
    node466_45(["function_definition"])
    node471_44(["external_declaration"])
    node476_43(["translation_unit"])
    node7_14 --> node12_34
    node12_34 --> node19_32
    node19_32 --> node466_45
    node23_51 --> node28_58
    node28_58 --> node95_58
    node33_131 --> node95_58
    node38_14 --> node43_34
    node43_34 --> node50_229
    node50_229 --> node72_232
    node54_51 --> node59_58
    node59_58 --> node66_332
    node66_332 --> node72_232
    node72_232 --> node77_231
    node77_231 --> node83_230
    node83_230 --> node95_58
    node87_335 --> node95_58
    node95_58 --> node102_57
    node102_57 --> node466_45
    node106_125 --> node459_129
    node111_208 --> node432_221
    node116_74 --> node121_92
    node121_92 --> node126_96
    node126_96 --> node133_150
    node133_150 --> node139_99
    node139_99 --> node144_100
    node144_100 --> node351_100
    node148_162 --> node351_100
    node153_74 --> node158_92
    node158_92 --> node163_96
    node163_96 --> node332_96
    node168_158 --> node332_96
    node173_74 --> node178_92
    node178_92 --> node183_96
    node183_96 --> node190_150
    node190_150 --> node196_99
    node196_99 --> node201_100
    node201_100 --> node207_101
    node207_101 --> node256_101
    node211_166 --> node256_101
    node216_75 --> node221_93
    node221_93 --> node226_92
    node226_92 --> node231_96
    node231_96 --> node238_97
    node238_97 --> node243_99
    node243_99 --> node248_281
    node248_281 --> node256_101
    node256_101 --> node262_102
    node262_102 --> node268_103
    node268_103 --> node274_104
    node274_104 --> node280_105
    node280_105 --> node286_106
    node286_106 --> node292_107
    node292_107 --> node298_108
    node298_108 --> node304_109
    node304_109 --> node310_151
    node310_151 --> node315_274
    node315_274 --> node320_273
    node320_273 --> node332_96
    node324_361 --> node332_96
    node332_96 --> node339_97
    node339_97 --> node344_277
    node344_277 --> node351_100
    node351_100 --> node357_101
    node357_101 --> node363_102
    node363_102 --> node369_103
    node369_103 --> node375_104
    node375_104 --> node381_105
    node381_105 --> node387_106
    node387_106 --> node393_107
    node393_107 --> node399_108
    node399_108 --> node405_109
    node405_109 --> node411_151
    node411_151 --> node416_152
    node416_152 --> node421_320
    node421_320 --> node432_221
    node425_392 --> node432_221
    node432_221 --> node437_213
    node437_213 --> node442_217
    node442_217 --> node447_216
    node447_216 --> node459_129
    node452_322 --> node459_129
    node459_129 --> node466_45
    node466_45 --> node471_44
    node471_44 --> node476_43
    node476_43 --> node2_0
```
