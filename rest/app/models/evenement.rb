class Evenement < ApplicationRecord
    has_one :adresses
    validates :title, presence: true, length: { minimum: 5 }
    validates :description, presence: true, length: { minimum: 20 }
end
