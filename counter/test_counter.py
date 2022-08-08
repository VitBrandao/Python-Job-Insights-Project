from counter import count_ocurrences


def test_counter():
    'Deve retornar a quantidade exata de ocorrências da palavra JavaScript'
    function_call = count_ocurrences("src/jobs.csv", "JavaScript")
    assert function_call == 122

    'Deve retornar a quantidade exata de ocorrências da palavra Python'
    function_call = count_ocurrences("src/jobs.csv", "Python")
    assert function_call == 1639

    'Não deve retornar a quantidade quando digitado incorretamente JavaScript'
    function_call = count_ocurrences("src/jobs.csv", "JavasScript")
    assert function_call != 122

    'Não deve retornar a quantidade quando digitado incorretamente Python'
    function_call = count_ocurrences("src/jobs.csv", "Pyton")
    assert function_call != 1639

    'Não deve diferenciar maiúsculas e minúsculas para JavaScript'
    function_call = count_ocurrences("src/jobs.csv", "javAsCriPt")
    assert function_call == 122

    'Não deve diferenciar maiúsculas e minúsculas para Python'
    function_call = count_ocurrences("src/jobs.csv", "pYtHOn")
    assert function_call == 1639
