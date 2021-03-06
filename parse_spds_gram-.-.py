from scripts.fasta import to_fasta, batch_to_fasta, batch_fasta_save
from scripts.fix_sequence import fix_sequences

def read_csv(file_path):
	IDs = None
	with open(file_path, 'r') as f:
		IDs = f.read().split('\n')
	IDs.pop(-1)

	IDs_ = []
	for i in IDs:
		if(i.split(',')[-1] is not 'S'):
			IDs_.append(i.split(',')[0])
	return IDs_

def read_fasta(file_path):
	Sequences = []
	with open(file_path, 'r') as f:
		Seqs = f.read().split('\n')
		f.close()
	Seqs.pop(-1)
	for i in range(0, len(Seqs), 2):
		Sequences.append((Seqs[i].split('>')[-1], Seqs[i + 1]))
	return Sequences

def pick_Sequences(IDs, Sequences):
	Sequences_ = []
	for i in IDs:
		for j in Sequences:
			if (j[0] == i):
				Sequences_.append(j)
	return Sequences_


if __name__ == '__main__':
	IDs = read_csv('gram-.spds17.csv')
	Sequences = read_fasta('gram-.spds17.fasta')
	print('At the begin we have %s sequences' % str(len(Sequences)))
	Sequences = pick_Sequences(IDs, Sequences)
	Sequences = fix_sequences(Sequences, 20)
	print('At the end we have %s sequences that contain signal peptide' % str(len(Sequences)))
	Sequences = batch_to_fasta(Sequences)
	print(Sequences)
	batch_fasta_save('parse_gram-.-.spds17.fasta', Sequences)
