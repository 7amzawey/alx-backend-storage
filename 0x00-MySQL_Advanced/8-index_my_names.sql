-- Create an index on fields starting letter
CREATE INDEX idx_name_first ON names (name(1));