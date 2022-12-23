# Qiskit

## Dependencies
```
qiskit-aer
qiskit-terra
matplotlib
numpy
pylatexenc
scipy
```
## Supported algorithms
### Simon's algorithm
```
python simons.py <n_qbits> <target_bit>
```
The implementation for Simon's algorithm used the unitary matrix of the. test circuit `flip_but_bit` to verify correctness.  `flip_but_bit` takes the number of q_bits (`n_qbits`) and a target bit (`target_bit`) as parameters.  It bit-flips the value of all other bits besides `target_bit`.

For example, the below circuit captures a circuit with `n_qbits=4` and `target_bit=2`.  Note that 8 q_bits appear in the circuit as required for Simon's circuit.

![Test circuit](images/flip_but_bit_circuit.png)
