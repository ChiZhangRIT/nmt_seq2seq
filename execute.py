import os

# more training on caption dataset, to get the best model.
command = 'python -m nmt.nmt \
--src=enc
--tgt=dec \
--vocab_prefix=nmt/nmt_data/_vocab50000  \
--train_prefix=nmt/nmt_data/_train_captions \
--dev_prefix=nmt/nmt_data/_train_captions_1000  \
--out_dir=nmt/nmt_model/caption_moreTrain \
--num_train_steps=1000000 \
--steps_per_stats=20000 \
--num_layers=3 \
--num_units=300 \
--dropout=0.2 \
--metrics=bleu \
--batch_size=256 \
--learning_rate=0.001 \
--optimizer=adam \
--decay_scheme=luong234 '
		
# # Experiment with full caption dataset.
# command = 'python -m nmt.nmt \
# 		--src=enc --tgt=dec \
# 		--vocab_prefix=nmt/nmt_data/_vocab50000  \
# 		--train_prefix=nmt/nmt_data/_train_captions \
# 		--dev_prefix=nmt/nmt_data/_train_captions_1000  \
# 		--out_dir=nmt/nmt_model/caption \
# 		--num_train_steps=200000 \
# 		--steps_per_stats=20000 \
# 		--num_layers=3 \
# 		--num_units=300 \
# 		--dropout=0.2 \
# 		--metrics=bleu \
# 		--batch_size=256 '

# # Experiment with 1000 samples. Try to overfit the model.
# command = 'python -m nmt.nmt \
# 		--src=enc --tgt=dec \
# 		--vocab_prefix=nmt/nmt_data/_vocab50000  \
# 		--train_prefix=nmt/nmt_data/_train_captions_1000 \
# 		--dev_prefix=nmt/nmt_data/_train_captions_1000  \
# 		--out_dir=nmt/nmt_model/caption \
# 		--num_train_steps=12000 \
# 		--steps_per_stats=100 \
# 		--num_layers=3 \
# 		--num_units=300 \
# 		--dropout=0.2 \
# 		--metrics=bleu \
# 		--batch_size=512 '

# # Moved data and model saving dir to nmt/. Working.
# command = 'python -m nmt.nmt \
# 		--src=vi --tgt=en \
# 		--vocab_prefix=nmt/nmt_data/vocab  \
# 		--train_prefix=nmt/nmt_data/train \
# 		--dev_prefix=nmt/nmt_data/tst2012  \
# 		--test_prefix=nmt/nmt_data/tst2013 \
# 		--out_dir=nmt/nmt_model/vi2en \
# 		--num_train_steps=12000 \
# 		--steps_per_stats=100 \
# 		--num_layers=2 \
# 		--num_units=128 \
# 		--dropout=0.2 \
# 		--metrics=bleu'

# # Original code to run viet2eng example.
# command = 'python -m nmt.nmt \
# 		--src=vi --tgt=en \
# 		--vocab_prefix=/tmp/nmt_data/vocab  \
# 		--train_prefix=/tmp/nmt_data/train \
# 		--dev_prefix=/tmp/nmt_data/tst2012  \
# 		--test_prefix=/tmp/nmt_data/tst2013 \
# 		--out_dir=/tmp/nmt_model \
# 		--num_train_steps=12000 \
# 		--steps_per_stats=100 \
# 		--num_layers=2 \
# 		--num_units=128 \
# 		--dropout=0.2 \
# 		--metrics=bleu'

os.system(command)
