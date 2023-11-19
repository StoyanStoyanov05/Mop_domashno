def calculate_similarity(model, base_word, target_word):
    if base_word not in model or target_word not in model:
        return None

    base_vector, target_vector = model[base_word], model[target_word]

    dot_product = sum(x * y for x, y in zip(base_vector, target_vector))
    magnitude_base = sum(x ** 2 for x in base_vector) ** 0.5
    magnitude_target = sum(x ** 2 for x in target_vector) ** 0.5

    if magnitude_base == 0 or magnitude_target == 0:
        return None

    return dot_product / (magnitude_base * magnitude_target)


def find_most_similar_to_given(model, given_word, target_words):
    similarities = [(word, calculate_similarity(model, given_word, word)) for word in target_words if word in model]
    if not similarities:
        return None

    most_similar_word = max(similarities, key=lambda x: x[1])[0]
    return most_similar_word


def doesnt_match(model, given_words):
    if len(given_words) < 2:
        return None

    word_to_compare, *rest = given_words
    max_similarity = float('-inf')
    odd_one_out = None

    for word in rest:
        similarity = calculate_similarity(model, word_to_compare, word)
        if similarity is not None and similarity > max_similarity:
            max_similarity = similarity
            odd_one_out = word

    return odd_one_out
