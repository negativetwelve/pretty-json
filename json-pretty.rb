require 'json'

puts JSON.pretty_generate(Hash[JSON.parse(STDIN.read).sort])
