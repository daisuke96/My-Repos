class Client < ApplicationRecord
    enum status: { "契約前": 0, "進行中": 1, "完了": 2 }

    validates :pj_name, :client_name, exclusion: { in: [nil, ""] }, length: { in: 3..80 }
    validates :status, inclusion: { in: ["契約前", "進行中", "完了"] }, exclusion: { in: [nil, ""] }
    validates :price, numericality: { only_integer: true },  exclusion: { in: [nil, ""] }
end
