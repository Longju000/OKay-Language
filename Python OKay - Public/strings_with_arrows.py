""" def string_with_arrows(text, pos_start, pos_end):
    lines = text.splitlines()
    result = []
    for i in range(pos_start.ln, pos_end.ln + 1):
        line = lines[i]
        start = pos_start.col if i == pos_start.ln else 0
        end = pos_end.col if i == pos_end.ln else len(line) - 1
        result.append(line[:start] + '^' * (end - start) + line[end:])
    return '\n'.join(result) """

#It uses the splitlines() method to split the text into lines, which is more efficient than using the find('\n') method repeatedly.
#It uses a for loop to iterate over the lines, rather than using a while loop.
#It uses the append() method to add lines to the result list, rather than concatenating strings with the + operator.
#It uses the join() method to join the lines in the result list with a newline character.

def string_with_arrows(text, pos_start, pos_end):
	result = ''

	# Calculate indices
	idx_start = max(text.rfind('\n', 0, pos_start.idx), 0)
	idx_end = text.find('\n', idx_start + 1)
	if idx_end < 0: idx_end = len(text)
	
	# Generate each line
	line_count = pos_end.ln - pos_start.ln + 1
	for i in range(line_count):
		# Calculate line columns
		line = text[idx_start:idx_end]
		col_start = pos_start.col if i == 0 else 0
		col_end = pos_end.col if i == line_count - 1 else len(line) - 1

		# Append to result
		result += line + '\n'
		result += ' ' * col_start + '^' * (col_end - col_start)

		# Re-calculate indices
		idx_start = idx_end
		idx_end = text.find('\n', idx_start + 1)
		if idx_end < 0: idx_end = len(text)

	return result.replace('\t', '')