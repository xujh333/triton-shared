import re

pattern = r"tt.func public @(\w+)\(.+"
matches = re.findall(pattern, '  tt.func public @_matmul_NNN_fp16xfp16xfp16_16x128x64(%arg0: !tt.ptr<f16> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg1: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg2: !tt.ptr<f16> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg3: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg4: !tt.ptr<f16> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg5: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg6: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg7: !tt.ptr<f32> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg8: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg9: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg10: i32 {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg11: !tt.ptr<i32> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg12: !tt.ptr<i32> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg13: !tt.ptr<i32> {tt.divisibility = 16 : i32} loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg14: !tt.ptr<i32> loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0), %arg15: !tt.ptr<i32> loc("/home/nhat/openai/export-model-runner/triton-inference/amdgpt/matmul.py":123:0)) attributes {noinline = false} {')
assert len(matches) == 1
name = matches[0]

print(name)
