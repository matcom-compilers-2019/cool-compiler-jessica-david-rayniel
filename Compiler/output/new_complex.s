.data
data_0:   .asciiz   "IO"
data_1:   .asciiz   "Object"
data_2:   .asciiz   "Main"
data_3:   .asciiz   "es de tipo dinamico mas justo Complex"
data_4:   .asciiz   "es de tipo dinamico mas justo IO"
data_5:   .asciiz   "es de tipo dinamico mas justo Object"
data_6:   .asciiz   "=(\n"
data_7:   .asciiz   "=)\n"
data_8:   .asciiz   "=(\n"
data_9:   .asciiz   "=)\n"
data_10:   .asciiz   "Complex"
data_11:   .asciiz   "I"
data_12:   .asciiz   "+"
mips_abort_message_of_mine:   .asciiz   "Se salio de la ejecucion debido a un abort de object"
mips_except_message_of_mine:   .asciiz   "Runtime Error, debido a algun error"
mips_constant_1 :  .word   2147483648
mips_constant_2 :  .word   5
mips_constant_3 :  .word   8
mips_constant_4 :  .word   1
mips_constant_5 :  .word   3
mips_constant_6 :  .word   0
mips_constant_7 :  .word   1
mips_constant_8 :  .word   0
mips_constant_9 :  .word   0
mips_constant_10 :  .word   0
mips_constant_11 :  .word   0
mips_constant_12 :  .word   1
mips_constant_13 :  .word   0
mips_constant_14 :  .word   0
mips_constant_15 :  .word   0
mips_constant_16 :  .word   1
mips_constant_17 :  .word   0
mips_constant_18 :  .word   0
mips_constant_19 :  .word   1
mips_constant_20 :  .word   1024
mips_constant_21 :  .word   0
mips_constant_22 :  .word   1
mips_constant_23 :  .word   1
mips_constant_24 :  .word   0
mips_constant_25 :  .word   8
mips_constant_26 :  .word   4
mips_constant_27 :  .word   2
mips_constant_28 :  .word   3
mips_constant_29 :  .word   0
mips_constant_30 :  .word   1
mips_constant_31 :  .word   4
mips_constant_32 :  .word   2
mips_constant_33 :  .word   3
mips_constant_34 :  .word   0
mips_constant_35 :  .word   6
mips_constant_36 :  .word   15
mips_constant_37 :  .word   1
mips_constant_38 :  .word   4
mips_constant_39 :  .word   9
mips_constant_40 :  .word   1
mips_constant_41 :  .word   2
mips_constant_42 :  .word   3
mips_constant_43 :  .word   0
mips_constant_44 :  .word   1
mips_constant_45 :  .word   1
mips_constant_46 :  .word   6
mips_constant_47 :  .word   15
mips_constant_48 :  .word   1
mips_constant_49 :  .word   2
mips_constant_50 :  .word   0
mips_constant_51 :  .word   4
mips_constant_52 :  .word   2
mips_constant_53 :  .word   2
mips_constant_54 :  .word   0
mips_constant_55 :  .word   2
mips_constant_56 :  .word   0
mips_constant_57 :  .word   2
mips_constant_58 :  .word   0
mips_constant_59 :  .word   2
mips_constant_60 :  .word   0
mips_constant_61 :  .word   2
mips_constant_62 :  .word   0
mips_constant_63 :  .word   2
mips_constant_64 :  .word   0
mips_constant_65 :  .word   0
mips_constant_66 :  .word   4
mips_constant_67 :  .word   0
mips_constant_68 :  .word   5
mips_constant_69 :  .word   11
mips_constant_70 :  .word   2
mips_constant_71 :  .word   2
mips_constant_72 :  .word   3
mips_constant_73 :  .word   0
mips_constant_74 :  .word   4
mips_constant_75 :  .word   5
mips_constant_76 :  .word   5
mips_constant_77 :  .word   0
mips_constant_78 :  .word   5
mips_constant_79 :  .word   4
mips_constant_80 :  .word   2
mips_constant_81 :  .word   0
mips_constant_82 :  .word   2
mips_constant_83 :  .word   0
mips_constant_84 :  .word   2
mips_constant_85 :  .word   0
mips_constant_86 :  .word   4
mips_constant_87 :  .word   4
mips_constant_88 :  .word   4
mips_constant_89 :  .word   5
mips_constant_90 :  .word   5
mips_constant_91 :  .word   5
mips_constant_92 :  .word   5
mips_constant_93 :  .word   4
mips_constant_94 :  .word   4
mips_constant_95 :  .word   4
mips_constant_96 :  .word   2
mips_constant_97 :  .word   0
mips_constant_98 :  .word   0
mips_constant_99 :  .word   5
mips_constant_100 :  .word   2
mips_constant_101 :  .word   0
mips_constant_102 :  .word   0
mips_constant_103 :  .word   1
mips_constant_104 :  .word   4
mips_constant_105 :  .word   5
.text
    
.globl   main
.ent     main
main:
subu $sp, $sp, 44
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 44
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t5, $a0
lw $a0, mips_constant_2   # nos pidieron poner la variable con nombre mips_constant_2
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_main_internal_0
move $a0, $t5
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_main_internal_0
jal function__attr_con_at_Main
sw $v0, 36($sp)   # nos pidieron poner la variable con nombre local_main_internal_3
move $t5, $a0
lw $a0, mips_constant_3   # nos pidieron poner la variable con nombre mips_constant_3
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_main_internal_1
move $a0, $t5
lw $a0, 28($sp)   # nos pidieron poner la variable con nombre local_main_internal_1
jal function__method_con_at_Main
sw $v0, 32($sp)   # nos pidieron poner la variable con nombre local_main_internal_2
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_main_internal_3
lw $t1, mips_constant_4   # nos pidieron poner la variable con nombre mips_constant_4
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_main_internal_2
sw  $t2, 0($t1)
lw $a0, 36($sp)   # nos pidieron poner la variable con nombre local_main_internal_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_main_internal_3
lw $t1, 4($t0)
lw $t2,28($t1)
jalr $t2
sw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_main_internal_4
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_main_internal_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 44
li $v0, 10
syscall
.end main
    
.globl   function_abort_at_Object
.ent     function_abort_at_Object
function_abort_at_Object:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t5, $a0
la $a0, mips_abort_message_of_mine   # nos pidieron poner la variable con nombre mips_abort_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
move $v0, $s0   # nos pidieron poner la variable con nombre param_function_abort_at_Object_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function_abort_at_Object
    
.globl   function_copy_at_Object
.ent     function_copy_at_Object
function_copy_at_Object:
subu $sp, $sp, 52
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 52
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_copy_at_Object_instance_0
lw $t1, mips_constant_5   # nos pidieron poner la variable con nombre mips_constant_5
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_type_size_0
move $t5, $a0
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_type_size_0
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_new_instance_1
move $a0, $t5
lw $t0, mips_constant_6   # nos pidieron poner la variable con nombre mips_constant_6
sw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
continuelabel_de_cil_unique1:
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
lw $t1, 24($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_type_size_0
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_cond_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_cond_3
bnez $t0, endlabel_de_cil_unique2
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_copy_at_Object_instance_0
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_attr_4
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_new_instance_1
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_attr_4
sw  $t2, 0($t1)
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_temp_times_5
lw $t0, mips_constant_7   # nos pidieron poner la variable con nombre mips_constant_7
sw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_internal_6
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_temp_times_5
lw $t1, 48($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_internal_6
addu $t2, $t0, $t1
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_times_2
j continuelabel_de_cil_unique1
endlabel_de_cil_unique2:
lw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_function_copy_at_Object_new_instance_1
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 52
jr $ra
.end function_copy_at_Object
    
.globl   function_type_name_at_Object
.ent     function_type_name_at_Object
function_type_name_at_Object:
subu $sp, $sp, 32
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 32
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_type_name_at_Object_self_0
lw $t1, mips_constant_8   # nos pidieron poner la variable con nombre mips_constant_8
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_type_name_at_Object_data_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_type_name_at_Object_data_0
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_type_name_at_Object_name_1
lw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_function_type_name_at_Object_name_1
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 32
jr $ra
.end function_type_name_at_Object
    
.globl   function_concat_at_String
.ent     function_concat_at_String
function_concat_at_String:
subu $sp, $sp, 76
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 76
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_9   # nos pidieron poner la variable con nombre mips_constant_9
sw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
lw $t0, mips_constant_10   # nos pidieron poner la variable con nombre mips_constant_10
sw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_second_index_8
lw $t0, mips_constant_11   # nos pidieron poner la variable con nombre mips_constant_11
sw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_10
lw $t0, mips_constant_12   # nos pidieron poner la variable con nombre mips_constant_12
sw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_11
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_concat_at_String_string1_0
jal function_length_at_String
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_length1_0
move $a0, $s1   # nos pidieron poner la variable con nombre param_function_concat_at_String_string2_1
jal function_length_at_String
sw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_length2_1
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_length1_0
lw $t1, 28($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_length2_1
addu $t2, $t0, $t1
sw $t2, 48($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_sum_6
lw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_sum_6
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 72($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_12
move $t5, $a0
lw $a0, 72($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_12
li $v0, 9
syscall
sw $v0, 44($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_result_5
move $a0, $t5 
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_result_5
lw $t1, 48($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_sum_6
addu $t1, $t1 , $t0
lw $t2, 64($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_10
sb  $t2, 0($t1)
continuelabel_de_cil_unique3:
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_concat_at_String_string1_0
lw $t1, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
lw $t1, 64($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_10
seq $t2, $t0, $t1
sw $t2, 52($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_cond_7
lw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_cond_7
bnez $t0, end1label_de_cil_unique4
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_result_5
lw $t1, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
addu $t1, $t1 , $t0
lw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
sb  $t2, 0($t1)
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
j continuelabel_de_cil_unique3
end1label_de_cil_unique4:
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_concat_at_String_string2_1
lw $t1, 56($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_second_index_8
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
lw $t1, 64($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_10
seq $t2, $t0, $t1
sw $t2, 52($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_cond_7
lw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_cond_7
bnez $t0, end2label_de_cil_unique5
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_result_5
lw $t1, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
addu $t1, $t1 , $t0
lw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_actual_char_2
sb  $t2, 0($t1)
lw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_second_index_8
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 56($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_second_index_8
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_temp_index_4
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_index_3
j end1label_de_cil_unique4
end2label_de_cil_unique5:
lw $v0, 44($sp)   # nos pidieron poner la variable con nombre local_function_concat_at_String_result_5
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 76
jr $ra
.end function_concat_at_String
    
.globl   function_length_at_String
.ent     function_length_at_String
function_length_at_String:
subu $sp, $sp, 56
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 56
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_13   # nos pidieron poner la variable con nombre mips_constant_13
sw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_index_2
lw $t0, mips_constant_14   # nos pidieron poner la variable con nombre mips_constant_14
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_length_0
continuelabel_de_cil_unique7:
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_length_at_String_string_0
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_index_2
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_actual_char_1
lw $t0, mips_constant_15   # nos pidieron poner la variable con nombre mips_constant_15
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_internal_4
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_actual_char_1
lw $t1, 40($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_internal_4
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_cond_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_cond_3
bnez $t0, endlabel_de_cil_unique6
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_length_0
sw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_temp_length_6
lw $t0, mips_constant_16   # nos pidieron poner la variable con nombre mips_constant_16
sw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_internal_7
lw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_temp_length_6
lw $t1, 52($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_internal_7
addu $t2, $t0, $t1
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_length_0
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_index_2
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_temp_index_5
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_temp_index_5
lw $t1, 52($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_internal_7
addu $t2, $t0, $t1
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_index_2
j continuelabel_de_cil_unique7
endlabel_de_cil_unique6:
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_length_at_String_length_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 56
jr $ra
.end function_length_at_String
    
.globl   function_substr_at_String
.ent     function_substr_at_String
function_substr_at_String:
subu $sp, $sp, 76
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 76
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_17   # nos pidieron poner la variable con nombre mips_constant_17
sw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_other_index_7
lw $t0, mips_constant_18   # nos pidieron poner la variable con nombre mips_constant_18
sw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_10
lw $t0, mips_constant_19   # nos pidieron poner la variable con nombre mips_constant_19
sw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_11
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_substr_at_String_self_0
jal function_length_at_String
sw $v0, 36($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_length_string_3
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
move $t1, $s2   # nos pidieron poner la variable con nombre param_function_substr_at_String_length_2
addu $t2, $t0, $t1
sw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_second_index_4
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
lw $t1, 64($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_10
slt $t2, $t0, $t1
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond1_0
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_length_string_3
lw $t1, 40($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_second_index_4
slt $t2, $t0, $t1
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond2_1
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond1_0
bnez $t0, error1label_de_cil_unique9
j continue1label_de_cil_unique11
error1label_de_cil_unique9:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
continue1label_de_cil_unique11:
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond2_1
bnez $t0, error2label_de_cil_unique10
j continue2label_de_cil_unique12
error2label_de_cil_unique10:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
continue2label_de_cil_unique12:
move $t0, $s2   # nos pidieron poner la variable con nombre param_function_substr_at_String_length_2
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 72($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_12
move $t5, $a0
lw $a0, 72($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_12
li $v0, 9
syscall
sw $v0, 44($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_substr_5
move $a0, $t5 
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_substr_5
move $t1, $s2   # nos pidieron poner la variable con nombre param_function_substr_at_String_length_2
addu $t1, $t1 , $t0
lw $t2, 64($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_10
sb  $t2, 0($t1)
continuelabel_de_cil_unique13:
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
lw $t1, 40($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_second_index_4
sge $t2, $t0, $t1
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond3_2
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_cond3_2
bnez $t0, endlabel_de_cil_unique8
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_substr_at_String_self_0
move $t1, $s1   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 48($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_actual_char_6
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_substr_5
lw $t1, 52($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_other_index_7
addu $t1, $t1 , $t0
lw $t2, 48($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_actual_char_6
sb  $t2, 0($t1)
lw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_other_index_7
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 60($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_temp_other_index_9
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
lw $t1, 68($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_internal_11
addu $t2, $t0, $t1
sw $t2, 56($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_temp_index_8
lw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_temp_index_8
move $s1, $t0   # nos pidieron poner la variable con nombre param_function_substr_at_String_index_1
lw $t0, 60($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_temp_other_index_9
sw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_other_index_7
j continuelabel_de_cil_unique13
endlabel_de_cil_unique8:
lw $v0, 44($sp)   # nos pidieron poner la variable con nombre local_function_substr_at_String_substr_5
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 76
jr $ra
.end function_substr_at_String
    
.globl   function_in_int_at_IO
.ent     function_in_int_at_IO
function_in_int_at_IO:
subu $sp, $sp, 28
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 28
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
li $v0 , 5
syscall
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_int_at_IO_return_value_0
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_int_at_IO_return_value_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 28
jr $ra
.end function_in_int_at_IO
    
.globl   function_in_string_at_IO
.ent     function_in_string_at_IO
function_in_string_at_IO:
subu $sp, $sp, 32
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 32
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_20   # nos pidieron poner la variable con nombre mips_constant_20
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_length_1
move $t5, $a0
lw $a0, 28($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_length_1
li $v0, 9
syscall
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_local_0
move $a0, $t5 
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_local_0
li $a1, 1024
li $v0, 8
syscall
move $t6, $a0
jal function_length_at_String
subu $a2, $v0, 1
li $a1, 0
move $a0, $t6
jal function_substr_at_String
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_local_0
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_in_string_at_IO_local_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 32
jr $ra
.end function_in_string_at_IO
    
.globl   function_out_int_at_IO
.ent     function_out_int_at_IO
function_out_int_at_IO:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t5, $a0
move $a0, $s1   # nos pidieron poner la variable con nombre param_function_out_int_at_IO_int_param_1
li $v0 , 1
syscall
move $a0, $t5
move $v0, $s0   # nos pidieron poner la variable con nombre param_function_out_int_at_IO_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function_out_int_at_IO
    
.globl   function_out_string_at_IO
.ent     function_out_string_at_IO
function_out_string_at_IO:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t5, $a0
move $a0, $s1   # nos pidieron poner la variable con nombre param_function_out_string_at_IO_string_param_1
li $v0 , 4
syscall
move $a0, $t5
move $v0, $s0   # nos pidieron poner la variable con nombre param_function_out_string_at_IO_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function_out_string_at_IO
    
.globl   function_equals_string_at_String
.ent     function_equals_string_at_String
function_equals_string_at_String:
subu $sp, $sp, 52
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 52
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_21   # nos pidieron poner la variable con nombre mips_constant_21
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_index_0
lw $t0, mips_constant_22   # nos pidieron poner la variable con nombre mips_constant_22
sw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_const1_6
continuelabel_de_cil_unique14:
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_equals_string_at_String_string1_0
lw $t1, 24($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_index_0
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_char1_1
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_equals_string_at_String_string2_1
lw $t1, 24($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_index_0
addu $t1, $t1 , $t0
li $t2, 0
lb $t2, 0($t1)
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_char2_2
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_char1_1
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_char2_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_cond_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_cond_3
bnez $t0, equalslabel_de_cil_unique15
j not_equallabel_de_cil_unique17
equalslabel_de_cil_unique15:
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_char1_1
bnez $t0, not_endlabel_de_cil_unique16
lw $t0, mips_constant_23   # nos pidieron poner la variable con nombre mips_constant_23
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_result_4
j endlabel_de_cil_unique18
not_endlabel_de_cil_unique16:
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_index_0
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_temp_index_5
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_temp_index_5
lw $t1, 48($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_const1_6
addu $t2, $t0, $t1
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_index_0
j continuelabel_de_cil_unique14
not_equallabel_de_cil_unique17:
lw $t0, mips_constant_24   # nos pidieron poner la variable con nombre mips_constant_24
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_result_4
endlabel_de_cil_unique18:
lw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_function_equals_string_at_String_result_4
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 52
jr $ra
.end function_equals_string_at_String
    
.globl   function__attr_con_at_IO
.ent     function__attr_con_at_IO
function__attr_con_at_IO:
subu $sp, $sp, 32
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 32
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_25   # nos pidieron poner la variable con nombre mips_constant_25
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_IO_begin_local_0
lw $t0, mips_constant_26   # nos pidieron poner la variable con nombre mips_constant_26
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_IO_len_local_1
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_IO_self_0
lw $t1, mips_constant_27   # nos pidieron poner la variable con nombre mips_constant_27
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_IO_begin_local_0
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_IO_self_0
lw $t1, mips_constant_28   # nos pidieron poner la variable con nombre mips_constant_28
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_IO_len_local_1
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_IO_self_0
lw $t1, mips_constant_29   # nos pidieron poner la variable con nombre mips_constant_29
sll $t1, $t1, 2
addu $t1, $t1 , $t0
la $t2, data_0   # nos pidieron poner la variable con nombre data_0
sw  $t2, 0($t1)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_IO_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 32
jr $ra
.end function__attr_con_at_IO
    
.globl   function__attr_con_at_Object
.ent     function__attr_con_at_Object
function__attr_con_at_Object:
subu $sp, $sp, 32
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 32
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_30   # nos pidieron poner la variable con nombre mips_constant_30
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Object_begin_local_0
lw $t0, mips_constant_31   # nos pidieron poner la variable con nombre mips_constant_31
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Object_len_local_1
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Object_self_0
lw $t1, mips_constant_32   # nos pidieron poner la variable con nombre mips_constant_32
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Object_begin_local_0
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Object_self_0
lw $t1, mips_constant_33   # nos pidieron poner la variable con nombre mips_constant_33
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Object_len_local_1
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Object_self_0
lw $t1, mips_constant_34   # nos pidieron poner la variable con nombre mips_constant_34
sll $t1, $t1, 2
addu $t1, $t1 , $t0
la $t2, data_1   # nos pidieron poner la variable con nombre data_1
sw  $t2, 0($t1)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Object_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 32
jr $ra
.end function__attr_con_at_Object
    
.globl   function__method_con_at_Object
.ent     function__method_con_at_Object
function__method_con_at_Object:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Object__vtable_0
la $t1, function_abort_at_Object
sw $t1, 0($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Object__vtable_0
la $t1, function_type_name_at_Object
sw $t1, 8($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Object__vtable_0
la $t1, function_copy_at_Object
sw $t1, 4($t0)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Object__vtable_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function__method_con_at_Object
    
.globl   function__method_con_at_IO
.ent     function__method_con_at_IO
function__method_con_at_IO:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_abort_at_Object
sw $t1, 0($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_type_name_at_Object
sw $t1, 8($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_copy_at_Object
sw $t1, 4($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_out_string_at_IO
sw $t1, 24($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_out_int_at_IO
sw $t1, 20($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_in_string_at_IO
sw $t1, 16($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
la $t1, function_in_int_at_IO
sw $t1, 12($t0)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_IO__vtable_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function__method_con_at_IO
    
.globl   function__attr_con_at_Main
.ent     function__attr_con_at_Main
function__attr_con_at_Main:
subu $sp, $sp, 60
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 60
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $a0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
jal function__attr_con_at_IO
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_0
move $s0, $t0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
move $t5, $a0
lw $a0, mips_constant_35   # nos pidieron poner la variable con nombre mips_constant_35
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 44($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_5
move $a0, $t5
lw $a0, 44($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_5
jal function__attr_con_at_Complex
sw $v0, 56($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_8
move $t5, $a0
lw $a0, mips_constant_36   # nos pidieron poner la variable con nombre mips_constant_36
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 48($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_6
move $a0, $t5
lw $a0, 48($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_6
jal function__method_con_at_Complex
sw $v0, 52($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_7
lw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_8
lw $t1, mips_constant_37   # nos pidieron poner la variable con nombre mips_constant_37
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 52($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_7
sw  $t2, 0($t1)
lw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_internal_8
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_io_4
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
lw $t1, mips_constant_38   # nos pidieron poner la variable con nombre mips_constant_38
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_io_4
sw  $t2, 0($t1)
lw $t0, mips_constant_39   # nos pidieron poner la variable con nombre mips_constant_39
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_begin_1
lw $t0, mips_constant_40   # nos pidieron poner la variable con nombre mips_constant_40
sw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_len_2
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
lw $t1, mips_constant_41   # nos pidieron poner la variable con nombre mips_constant_41
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_begin_1
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
lw $t1, mips_constant_42   # nos pidieron poner la variable con nombre mips_constant_42
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Main_len_2
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
lw $t1, mips_constant_43   # nos pidieron poner la variable con nombre mips_constant_43
sll $t1, $t1, 2
addu $t1, $t1 , $t0
la $t2, data_2   # nos pidieron poner la variable con nombre data_2
sw  $t2, 0($t1)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Main_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 60
jr $ra
.end function__attr_con_at_Main
    
.globl   function__method_con_at_Main
.ent     function__method_con_at_Main
function__method_con_at_Main:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_abort_at_Object
sw $t1, 0($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_copy_at_Object
sw $t1, 4($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_type_name_at_Object
sw $t1, 8($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_in_int_at_IO
sw $t1, 12($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_in_string_at_IO
sw $t1, 16($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_out_int_at_IO
sw $t1, 20($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_out_string_at_IO
sw $t1, 24($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
la $t1, function_main_at_Main
sw $t1, 28($t0)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Main__vtable_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function__method_con_at_Main
    
.globl   function_main_at_Main
.ent     function_main_at_Main
function_main_at_Main:
subu $sp, $sp, 296
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 296
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
lw $t0, mips_constant_44   # nos pidieron poner la variable con nombre mips_constant_44
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_5
lw $t0, mips_constant_45   # nos pidieron poner la variable con nombre mips_constant_45
sw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_6
move $t5, $a0
lw $a0, mips_constant_46   # nos pidieron poner la variable con nombre mips_constant_46
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 52($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_7
move $a0, $t5
lw $a0, 52($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_7
jal function__attr_con_at_Complex
sw $v0, 64($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_10
move $t5, $a0
lw $a0, mips_constant_47   # nos pidieron poner la variable con nombre mips_constant_47
sll $a0, $a0, 2
li $v0, 9
syscall
sw $v0, 56($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_8
move $a0, $t5
lw $a0, 56($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_8
jal function__method_con_at_Complex
sw $v0, 60($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_9
lw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_10
lw $t1, mips_constant_48   # nos pidieron poner la variable con nombre mips_constant_48
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 60($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_9
sw  $t2, 0($t1)
lw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_10
lw $t1, mips_constant_49   # nos pidieron poner la variable con nombre mips_constant_49
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_2
lw $t0, mips_constant_50   # nos pidieron poner la variable con nombre mips_constant_50
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_4
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_2
lw $t1, 40($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_4
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_3
bnez $t0, is_void1label_de_cil_unique19
j end_dispatch1label_de_cil_unique20
is_void1label_de_cil_unique19:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch1label_de_cil_unique20:
lw $a0, 64($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_10
lw $a1, 44($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_5
lw $a2, 48($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_6
lw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_10
lw $t1, 4($t0)
lw $t2,28($t1)
jalr $t2
sw $v0, 28($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_1
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_1
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, mips_constant_51   # nos pidieron poner la variable con nombre mips_constant_51
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 68($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_11
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_11
lw $t1, mips_constant_52   # nos pidieron poner la variable con nombre mips_constant_52
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 11   # nos pidieron poner la variable de tipo int igual a = 11
sge $t2, $t0, $t1
sw $t2, 80($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_14
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 12   # nos pidieron poner la variable de tipo int igual a = 12
sle $t2, $t0, $t1
sw $t2, 84($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_15
lw $t0, 80($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_14
lw $t1, 84($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_15
and $t2, $t0, $t1
sw $t2, 88($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_16
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 8   # nos pidieron poner la variable de tipo int igual a = 8
sge $t2, $t0, $t1
sw $t2, 92($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_17
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 13   # nos pidieron poner la variable de tipo int igual a = 13
sle $t2, $t0, $t1
sw $t2, 96($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_18
lw $t0, 92($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_17
lw $t1, 96($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_18
and $t2, $t0, $t1
sw $t2, 100($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_19
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 1   # nos pidieron poner la variable de tipo int igual a = 1
sge $t2, $t0, $t1
sw $t2, 104($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_20
lw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_13
li $t1, 14   # nos pidieron poner la variable de tipo int igual a = 14
sle $t2, $t0, $t1
sw $t2, 108($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_21
lw $t0, 104($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_20
lw $t1, 108($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_21
and $t2, $t0, $t1
sw $t2, 112($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_22
lw $t0, 88($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_16
bnez $t0, branch0_1label_de_cil_unique22
j next0_1label_de_cil_unique23
branch0_1label_de_cil_unique22:
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_11
sw $t0, 116($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_tg_23
la $t0, data_3   # nos pidieron poner la variable con nombre data_3
sw $t0, 120($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_24
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 120($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_24
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 124($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_25
lw $t0, 124($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_25
sw $t0, 72($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_12
j end_case1label_de_cil_unique21
next0_1label_de_cil_unique23:
lw $t0, 100($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_19
bnez $t0, branch1_1label_de_cil_unique24
j next1_1label_de_cil_unique25
branch1_1label_de_cil_unique24:
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_11
sw $t0, 128($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_tg_26
la $t0, data_4   # nos pidieron poner la variable con nombre data_4
sw $t0, 132($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_27
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 132($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_27
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 136($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_28
lw $t0, 136($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_28
sw $t0, 72($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_12
j end_case1label_de_cil_unique21
next1_1label_de_cil_unique25:
lw $t0, 112($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_22
bnez $t0, branch2_1label_de_cil_unique26
j next2_1label_de_cil_unique27
branch2_1label_de_cil_unique26:
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_11
sw $t0, 140($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_tg_29
la $t0, data_5   # nos pidieron poner la variable con nombre data_5
sw $t0, 144($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_30
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 144($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_30
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 148($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_31
lw $t0, 148($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_31
sw $t0, 72($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_12
j end_case1label_de_cil_unique21
next2_1label_de_cil_unique27:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_case1label_de_cil_unique21:
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, mips_constant_53   # nos pidieron poner la variable con nombre mips_constant_53
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 160($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_34
lw $t0, mips_constant_54   # nos pidieron poner la variable con nombre mips_constant_54
sw $t0, 168($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_36
lw $t0, 160($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_34
lw $t1, 168($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_36
seq $t2, $t0, $t1
sw $t2, 164($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_35
lw $t0, 164($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_35
bnez $t0, is_void2label_de_cil_unique28
j end_dispatch2label_de_cil_unique29
is_void2label_de_cil_unique28:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch2label_de_cil_unique29:
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, 4($t0)
lw $t2,40($t1)
jalr $t2
sw $v0, 156($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_33
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, mips_constant_55   # nos pidieron poner la variable con nombre mips_constant_55
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 176($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_38
lw $t0, mips_constant_56   # nos pidieron poner la variable con nombre mips_constant_56
sw $t0, 184($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_40
lw $t0, 176($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_38
lw $t1, 184($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_40
seq $t2, $t0, $t1
sw $t2, 180($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_39
lw $t0, 180($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_39
bnez $t0, is_void3label_de_cil_unique30
j end_dispatch3label_de_cil_unique31
is_void3label_de_cil_unique30:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch3label_de_cil_unique31:
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, 4($t0)
lw $t2,36($t1)
jalr $t2
sw $v0, 172($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_37
lw $t0, 156($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_33
lw $t1, 172($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_37
seq $t2, $t0, $t1
sw $t2, 188($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_41
lw $t0, 188($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_41
bnez $t0, after_0label_de_cil_unique32
la $t0, data_6   # nos pidieron poner la variable con nombre data_6
sw $t0, 192($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_42
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 192($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_42
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 196($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_43
lw $t0, 196($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_43
sw $t0, 152($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_32
j endif_0label_de_cil_unique33
after_0label_de_cil_unique32:
la $t0, data_7   # nos pidieron poner la variable con nombre data_7
sw $t0, 200($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_44
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 200($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_44
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 204($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_45
lw $t0, 204($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_45
sw $t0, 152($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_32
endif_0label_de_cil_unique33:
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, mips_constant_57   # nos pidieron poner la variable con nombre mips_constant_57
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 232($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_52
lw $t0, mips_constant_58   # nos pidieron poner la variable con nombre mips_constant_58
sw $t0, 240($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_54
lw $t0, 232($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_52
lw $t1, 240($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_54
seq $t2, $t0, $t1
sw $t2, 236($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_53
lw $t0, 236($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_53
bnez $t0, is_void5label_de_cil_unique36
j end_dispatch5label_de_cil_unique37
is_void5label_de_cil_unique36:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch5label_de_cil_unique37:
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, 4($t0)
lw $t2,36($t1)
jalr $t2
sw $v0, 228($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_51
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, mips_constant_59   # nos pidieron poner la variable con nombre mips_constant_59
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 264($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_60
lw $t0, mips_constant_60   # nos pidieron poner la variable con nombre mips_constant_60
sw $t0, 272($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_62
lw $t0, 264($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_60
lw $t1, 272($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_62
seq $t2, $t0, $t1
sw $t2, 268($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_61
lw $t0, 268($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_61
bnez $t0, is_void7label_de_cil_unique40
j end_dispatch7label_de_cil_unique41
is_void7label_de_cil_unique40:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch7label_de_cil_unique41:
lw $a0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_c_0
lw $t1, 4($t0)
lw $t2,40($t1)
jalr $t2
sw $v0, 260($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_59
lw $t0, 260($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_59
lw $t1, mips_constant_61   # nos pidieron poner la variable con nombre mips_constant_61
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 248($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_56
lw $t0, mips_constant_62   # nos pidieron poner la variable con nombre mips_constant_62
sw $t0, 256($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_58
lw $t0, 248($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_56
lw $t1, 256($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_58
seq $t2, $t0, $t1
sw $t2, 252($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_57
lw $t0, 252($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_57
bnez $t0, is_void6label_de_cil_unique38
j end_dispatch6label_de_cil_unique39
is_void6label_de_cil_unique38:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch6label_de_cil_unique39:
lw $a0, 260($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_59
lw $t0, 260($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_59
lw $t1, 4($t0)
lw $t2,44($t1)
jalr $t2
sw $v0, 244($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_55
lw $t0, 244($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_55
lw $t1, mips_constant_63   # nos pidieron poner la variable con nombre mips_constant_63
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 216($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_48
lw $t0, mips_constant_64   # nos pidieron poner la variable con nombre mips_constant_64
sw $t0, 224($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_50
lw $t0, 216($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_48
lw $t1, 224($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_50
seq $t2, $t0, $t1
sw $t2, 220($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_49
lw $t0, 220($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_49
bnez $t0, is_void4label_de_cil_unique34
j end_dispatch4label_de_cil_unique35
is_void4label_de_cil_unique34:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch4label_de_cil_unique35:
lw $a0, 244($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_55
lw $a1, 228($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_51
lw $t0, 244($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_55
lw $t1, 4($t0)
lw $t2,48($t1)
jalr $t2
sw $v0, 212($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_47
lw $t0, 212($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_47
bnez $t0, after_1label_de_cil_unique42
la $t0, data_8   # nos pidieron poner la variable con nombre data_8
sw $t0, 276($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_63
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 276($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_63
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 280($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_64
lw $t0, 280($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_64
sw $t0, 208($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_46
j endif_1label_de_cil_unique43
after_1label_de_cil_unique42:
la $t0, data_9   # nos pidieron poner la variable con nombre data_9
sw $t0, 284($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_65
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $a1, 284($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_65
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_main_at_Main_self_0
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 288($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_66
lw $t0, 288($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_66
sw $t0, 208($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_46
endif_1label_de_cil_unique43:
lw $t0, 208($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_46
sw $t0, 292($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_67
lw $v0, 292($sp)   # nos pidieron poner la variable con nombre local_function_main_at_Main_internal_67
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 296
jr $ra
.end function_main_at_Main
    
.globl   function__attr_con_at_Complex
.ent     function__attr_con_at_Complex
function__attr_con_at_Complex:
subu $sp, $sp, 48
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 48
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $a0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
jal function__attr_con_at_IO
sw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_internal_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_internal_0
move $s0, $t0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t0, mips_constant_65   # nos pidieron poner la variable con nombre mips_constant_65
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_x_4
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t1, mips_constant_66   # nos pidieron poner la variable con nombre mips_constant_66
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_x_4
sw  $t2, 0($t1)
lw $t0, mips_constant_67   # nos pidieron poner la variable con nombre mips_constant_67
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_y_5
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t1, mips_constant_68   # nos pidieron poner la variable con nombre mips_constant_68
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 44($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_y_5
sw  $t2, 0($t1)
lw $t0, mips_constant_69   # nos pidieron poner la variable con nombre mips_constant_69
sw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_begin_1
lw $t0, mips_constant_70   # nos pidieron poner la variable con nombre mips_constant_70
sw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_len_2
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t1, mips_constant_71   # nos pidieron poner la variable con nombre mips_constant_71
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_begin_1
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t1, mips_constant_72   # nos pidieron poner la variable con nombre mips_constant_72
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function__attr_con_at_Complex_len_2
sw  $t2, 0($t1)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $t1, mips_constant_73   # nos pidieron poner la variable con nombre mips_constant_73
sll $t1, $t1, 2
addu $t1, $t1 , $t0
la $t2, data_10   # nos pidieron poner la variable con nombre data_10
sw  $t2, 0($t1)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__attr_con_at_Complex_self_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 48
jr $ra
.end function__attr_con_at_Complex
    
.globl   function__method_con_at_Complex
.ent     function__method_con_at_Complex
function__method_con_at_Complex:
subu $sp, $sp, 24
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 24
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_abort_at_Object
sw $t1, 0($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_copy_at_Object
sw $t1, 4($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_type_name_at_Object
sw $t1, 8($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_in_int_at_IO
sw $t1, 12($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_in_string_at_IO
sw $t1, 16($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_out_int_at_IO
sw $t1, 20($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_out_string_at_IO
sw $t1, 24($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_init_at_Complex
sw $t1, 28($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_print_at_Complex
sw $t1, 32($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_reflect_0_at_Complex
sw $t1, 36($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_reflect_X_at_Complex
sw $t1, 40($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_reflect_Y_at_Complex
sw $t1, 44($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_equal_at_Complex
sw $t1, 48($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_x_value_at_Complex
sw $t1, 52($t0)
move $t0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
la $t1, function_y_value_at_Complex
sw $t1, 56($t0)
move $v0, $s0   # nos pidieron poner la variable con nombre param_function__method_con_at_Complex__vtable_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 24
jr $ra
.end function__method_con_at_Complex
    
.globl   function_init_at_Complex
.ent     function_init_at_Complex
function_init_at_Complex:
subu $sp, $sp, 44
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 44
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_init_at_Complex_self_0
lw $t1, mips_constant_74   # nos pidieron poner la variable con nombre mips_constant_74
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_0
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_0
move $t1, $s1   # nos pidieron poner la variable con nombre param_function_init_at_Complex_a_1
seq $t2, $t0, $t1
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_1
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_init_at_Complex_self_0
lw $t1, mips_constant_75   # nos pidieron poner la variable con nombre mips_constant_75
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 32($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_2
lw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_2
move $t1, $s2   # nos pidieron poner la variable con nombre param_function_init_at_Complex_b_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_init_at_Complex_self_0
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_4
lw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_function_init_at_Complex_internal_4
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 44
jr $ra
.end function_init_at_Complex
    
.globl   function_print_at_Complex
.ent     function_print_at_Complex
function_print_at_Complex:
subu $sp, $sp, 116
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 116
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, mips_constant_76   # nos pidieron poner la variable con nombre mips_constant_76
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_1
lw $t0, mips_constant_77   # nos pidieron poner la variable con nombre mips_constant_77
sw $t0, 32($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_2
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_1
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_3
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_3
bnez $t0, after_2label_de_cil_unique44
la $t0, data_11   # nos pidieron poner la variable con nombre data_11
sw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_8
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, mips_constant_78   # nos pidieron poner la variable con nombre mips_constant_78
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 76($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_13
la $t0, data_12   # nos pidieron poner la variable con nombre data_12
sw $t0, 96($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_18
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, mips_constant_79   # nos pidieron poner la variable con nombre mips_constant_79
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 100($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_19
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $a1, 100($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_19
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, 4($t0)
lw $t2,20($t1)
jalr $t2
sw $v0, 104($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_20
lw $t0, 104($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_20
lw $t1, mips_constant_80   # nos pidieron poner la variable con nombre mips_constant_80
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 84($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_15
lw $t0, mips_constant_81   # nos pidieron poner la variable con nombre mips_constant_81
sw $t0, 92($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_17
lw $t0, 84($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_15
lw $t1, 92($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_17
seq $t2, $t0, $t1
sw $t2, 88($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_16
lw $t0, 88($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_16
bnez $t0, is_void10label_de_cil_unique50
j end_dispatch10label_de_cil_unique51
is_void10label_de_cil_unique50:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch10label_de_cil_unique51:
lw $a0, 104($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_20
lw $a1, 96($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_18
lw $t0, 104($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_20
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 80($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_14
lw $t0, 80($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_14
lw $t1, mips_constant_82   # nos pidieron poner la variable con nombre mips_constant_82
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 64($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_10
lw $t0, mips_constant_83   # nos pidieron poner la variable con nombre mips_constant_83
sw $t0, 72($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_12
lw $t0, 64($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_10
lw $t1, 72($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_12
seq $t2, $t0, $t1
sw $t2, 68($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_11
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_11
bnez $t0, is_void9label_de_cil_unique48
j end_dispatch9label_de_cil_unique49
is_void9label_de_cil_unique48:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch9label_de_cil_unique49:
lw $a0, 80($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_14
lw $a1, 76($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_13
lw $t0, 80($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_14
lw $t1, 4($t0)
lw $t2,20($t1)
jalr $t2
sw $v0, 60($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_9
lw $t0, 60($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_9
lw $t1, mips_constant_84   # nos pidieron poner la variable con nombre mips_constant_84
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 44($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_5
lw $t0, mips_constant_85   # nos pidieron poner la variable con nombre mips_constant_85
sw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_7
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_5
lw $t1, 52($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_7
seq $t2, $t0, $t1
sw $t2, 48($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_6
lw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_6
bnez $t0, is_void8label_de_cil_unique46
j end_dispatch8label_de_cil_unique47
is_void8label_de_cil_unique46:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch8label_de_cil_unique47:
lw $a0, 60($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_9
lw $a1, 56($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_8
lw $t0, 60($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_9
lw $t1, 4($t0)
lw $t2,24($t1)
jalr $t2
sw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_4
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_4
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_0
j endif_2label_de_cil_unique45
after_2label_de_cil_unique44:
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, mips_constant_86   # nos pidieron poner la variable con nombre mips_constant_86
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 108($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_21
move $a0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $a1, 108($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_21
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_print_at_Complex_self_0
lw $t1, 4($t0)
lw $t2,20($t1)
jalr $t2
sw $v0, 112($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_22
lw $t0, 112($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_22
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_0
endif_2label_de_cil_unique45:
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_print_at_Complex_internal_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 116
jr $ra
.end function_print_at_Complex
    
.globl   function_reflect_0_at_Complex
.ent     function_reflect_0_at_Complex
function_reflect_0_at_Complex:
subu $sp, $sp, 60
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 60
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_0_at_Complex_self_0
lw $t1, mips_constant_87   # nos pidieron poner la variable con nombre mips_constant_87
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_0
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_0_at_Complex_self_0
lw $t1, mips_constant_88   # nos pidieron poner la variable con nombre mips_constant_88
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_1
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_1
neg $t1, $t0
addi $t1, $t1, 1
sw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_2
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_0
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_0_at_Complex_self_0
lw $t1, mips_constant_89   # nos pidieron poner la variable con nombre mips_constant_89
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_4
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_0_at_Complex_self_0
lw $t1, mips_constant_90   # nos pidieron poner la variable con nombre mips_constant_90
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 44($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_5
lw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_5
neg $t1, $t0
addi $t1, $t1, 1
sw $t1, 48($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_6
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_4
lw $t1, 48($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_6
seq $t2, $t0, $t1
sw $t2, 52($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_7
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_0_at_Complex_self_0
sw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_8
lw $v0, 56($sp)   # nos pidieron poner la variable con nombre local_function_reflect_0_at_Complex_internal_8
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 60
jr $ra
.end function_reflect_0_at_Complex
    
.globl   function_reflect_X_at_Complex
.ent     function_reflect_X_at_Complex
function_reflect_X_at_Complex:
subu $sp, $sp, 44
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 44
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_X_at_Complex_self_0
lw $t1, mips_constant_91   # nos pidieron poner la variable con nombre mips_constant_91
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_0
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_X_at_Complex_self_0
lw $t1, mips_constant_92   # nos pidieron poner la variable con nombre mips_constant_92
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_1
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_1
neg $t1, $t0
addi $t1, $t1, 1
sw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_2
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_0
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_X_at_Complex_self_0
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_4
lw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_X_at_Complex_internal_4
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 44
jr $ra
.end function_reflect_X_at_Complex
    
.globl   function_reflect_Y_at_Complex
.ent     function_reflect_Y_at_Complex
function_reflect_Y_at_Complex:
subu $sp, $sp, 44
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 44
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_Y_at_Complex_self_0
lw $t1, mips_constant_93   # nos pidieron poner la variable con nombre mips_constant_93
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_0
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_Y_at_Complex_self_0
lw $t1, mips_constant_94   # nos pidieron poner la variable con nombre mips_constant_94
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_1
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_1
neg $t1, $t0
addi $t1, $t1, 1
sw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_2
lw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_0
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_2
seq $t2, $t0, $t1
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_reflect_Y_at_Complex_self_0
sw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_4
lw $v0, 40($sp)   # nos pidieron poner la variable con nombre local_function_reflect_Y_at_Complex_internal_4
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 44
jr $ra
.end function_reflect_Y_at_Complex
    
.globl   function_equal_at_Complex
.ent     function_equal_at_Complex
function_equal_at_Complex:
subu $sp, $sp, 92
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 92
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_self_0
lw $t1, mips_constant_95   # nos pidieron poner la variable con nombre mips_constant_95
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 28($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_1
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
lw $t1, mips_constant_96   # nos pidieron poner la variable con nombre mips_constant_96
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 36($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_3
lw $t0, mips_constant_97   # nos pidieron poner la variable con nombre mips_constant_97
sw $t0, 44($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_5
lw $t0, 36($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_3
lw $t1, 44($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_5
seq $t2, $t0, $t1
sw $t2, 40($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_4
lw $t0, 40($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_4
bnez $t0, is_void11label_de_cil_unique52
j end_dispatch11label_de_cil_unique53
is_void11label_de_cil_unique52:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch11label_de_cil_unique53:
move $a0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
lw $t1, 4($t0)
lw $t2,52($t1)
jalr $t2
sw $v0, 32($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_2
lw $t0, 28($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_1
lw $t1, 32($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_2
seq $t2, $t0, $t1
sw $t2, 48($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_6
lw $t0, 48($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_6
bnez $t0, after_3label_de_cil_unique54
lw $t0, mips_constant_98   # nos pidieron poner la variable con nombre mips_constant_98
sw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_7
lw $t0, 52($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_7
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_0
j endif_3label_de_cil_unique55
after_3label_de_cil_unique54:
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_self_0
lw $t1, mips_constant_99   # nos pidieron poner la variable con nombre mips_constant_99
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 60($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_9
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
lw $t1, mips_constant_100   # nos pidieron poner la variable con nombre mips_constant_100
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 68($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_11
lw $t0, mips_constant_101   # nos pidieron poner la variable con nombre mips_constant_101
sw $t0, 76($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_13
lw $t0, 68($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_11
lw $t1, 76($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_13
seq $t2, $t0, $t1
sw $t2, 72($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_12
lw $t0, 72($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_12
bnez $t0, is_void12label_de_cil_unique56
j end_dispatch12label_de_cil_unique57
is_void12label_de_cil_unique56:
move $t5, $a0
la $a0, mips_except_message_of_mine   # nos pidieron poner la variable con nombre mips_except_message_of_mine
li $v0 , 4
syscall
move $a0, $t5
li $v0 , 10
syscall
end_dispatch12label_de_cil_unique57:
move $a0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
move $t0, $s1   # nos pidieron poner la variable con nombre param_function_equal_at_Complex_d_1
lw $t1, 4($t0)
lw $t2,56($t1)
jalr $t2
sw $v0, 64($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_10
lw $t0, 60($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_9
lw $t1, 64($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_10
seq $t2, $t0, $t1
sw $t2, 80($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_14
lw $t0, 80($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_14
bnez $t0, after_4label_de_cil_unique58
lw $t0, mips_constant_102   # nos pidieron poner la variable con nombre mips_constant_102
sw $t0, 84($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_15
lw $t0, 84($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_15
sw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_8
j endif_4label_de_cil_unique59
after_4label_de_cil_unique58:
lw $t0, mips_constant_103   # nos pidieron poner la variable con nombre mips_constant_103
sw $t0, 88($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_16
lw $t0, 88($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_16
sw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_8
endif_4label_de_cil_unique59:
lw $t0, 56($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_8
sw $t0, 24($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_0
endif_3label_de_cil_unique55:
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_equal_at_Complex_internal_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 92
jr $ra
.end function_equal_at_Complex
    
.globl   function_x_value_at_Complex
.ent     function_x_value_at_Complex
function_x_value_at_Complex:
subu $sp, $sp, 28
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 28
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_x_value_at_Complex_self_0
lw $t1, mips_constant_104   # nos pidieron poner la variable con nombre mips_constant_104
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_x_value_at_Complex_internal_0
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_x_value_at_Complex_internal_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 28
jr $ra
.end function_x_value_at_Complex
    
.globl   function_y_value_at_Complex
.ent     function_y_value_at_Complex
function_y_value_at_Complex:
subu $sp, $sp, 28
sw $fp, 0($sp)
sw $ra, 4($sp)
sw $s0 8($sp)
sw $s1 12($sp)
sw $s2 16($sp)
sw $s3 20($sp)
addu $fp, $sp, 28
move $s0, $a0
move $s1, $a1
move $s2, $a2
move $s3, $a3
move $t0, $s0   # nos pidieron poner la variable con nombre param_function_y_value_at_Complex_self_0
lw $t1, mips_constant_105   # nos pidieron poner la variable con nombre mips_constant_105
sll $t1, $t1, 2
addu $t1, $t1 , $t0
lw $t2, 0($t1)
sw $t2, 24($sp)   # nos pidieron poner la variable con nombre local_function_y_value_at_Complex_internal_0
lw $v0, 24($sp)   # nos pidieron poner la variable con nombre local_function_y_value_at_Complex_internal_0
lw $fp, 0($sp)
lw $ra, 4($sp)
lw $s0 8($sp)
lw $s1 12($sp)
lw $s2 16($sp)
lw $s3 20($sp)
addu $sp, $sp, 28
jr $ra
.end function_y_value_at_Complex
