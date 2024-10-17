import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40  
context.generate_galois_keys()  


enc_num1 = ts.ckks_vector(context, [75])
enc_num2 = ts.ckks_vector(context, [326])

enc_result = enc_num1 + enc_num2

result = enc_result.decrypt()


rounded_result = round(result[0])

print(f"De som is: {rounded_result}")
