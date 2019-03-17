import hyrnn
import torch


def test_MobiusGRU_no_packed_just_works():
    input_size = 4
    hidden_size = 3
    gru = hyrnn.nets.MobiusGRU(
            input_size,
            hidden_size,
            hyperbolic_input=False)
    timestops = 10
    sequence = torch.randn(timestops, 5, input_size)
    h, ht = gru(sequence)
<<<<<<< HEAD
    assert h.shape[0] == 10
    assert ht.shape[1] == 5


def test_extract_last_states():
    tens = torch.tensor([[0, 1, 2, 3],
                        [4, 5, 6, 7],
                        [8, 9, 10, 11],
                        [12, 13, 14, 15],
                        [16, 17, 18, 19]])
    bs = torch.tensor([4, 4, 3, 2, 1])
    res = hyrnn.util.extract_last_states(tens, bs)
    assert (res == torch.tensor([16, 13, 10,  7])).all()
    res1 = hyrnn.util.extract_last_states(tens, bs-1)
    assert (res1 == torch.tensor([12,  9,  6,  3])).all()
=======
    assert h.shape[0] == timestops
    assert ht.shape[0] == 5


def test_mobius_gru_loop_just_works():
    input_size = 4
    hidden_size = 3
    seqs = torch.nn.utils.rnn.pack_sequence([
        torch.zeros(10, input_size),
        torch.zeros(5, input_size),
        torch.zeros(1, input_size)
        ])
    data, batch_sizes = seqs
    loop_params = dict()
    loop_params['h0'] = torch.zeros(input_size, requires_grad=False)
    loop_params['input'] = data
    loop_params['weight_ih'] = torch.nn.Parameter(
            torch.randn(3*hidden_size, input_size))
    loop_params['weight_hh'] = torch.nn.Parameter(
            torch.randn(3*hidden_size, hidden_size))
    loop_params['bias'] = torch.randn(3, hidden_size)
    loop_params['c'] = 1.
    loop_params['nonlin'] = None
    loop_params['hyperbolic_input'] = True
    loop_params['hyperbolic_hidden_state0'] = True
    outs = hyrnn.nets.mobius_gru_loop(**loop_params)

    print(outs.shape)


def test_MobiusGRU_with_packed_just_works():
    input_size = 4
    hidden_size = 3
    gru = hyrnn.nets.MobiusGRU(input_size,
            hidden_size,
            hyperbolic_input=False)
    seqs = torch.nn.utils.rnn.pack_sequence([
        torch.zeros(10, input_size),
        torch.zeros(5, input_size),
        torch.zeros(1, input_size)
        ])
    h, ht = gru(seqs)
    assert h.size(0) == 10 # max time
    print(h.shape)
    print(ht.shape)
>>>>>>> origin/ordering