class AddUrlTicketToEvenement < ActiveRecord::Migration[5.0]
  def change
    add_column :evenements, :url_ticket, :string
  end
end
