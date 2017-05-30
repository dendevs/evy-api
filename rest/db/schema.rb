# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170524133156) do

  create_table "adresses", force: :cascade do |t|
    t.string   "pays"
    t.string   "province"
    t.string   "code_postal"
    t.string   "ville"
    t.string   "rue"
    t.string   "numero"
    t.string   "boite"
    t.string   "complement"
    t.decimal  "latitude",     precision: 5, scale: 2
    t.decimal  "longitude",    precision: 5, scale: 2
    t.integer  "evenement_id"
    t.datetime "created_at",                           null: false
    t.datetime "updated_at",                           null: false
    t.index ["evenement_id"], name: "index_adresses_on_evenement_id"
  end

  create_table "evenements", force: :cascade do |t|
    t.string   "title"
    t.text     "description"
    t.datetime "created_at",    null: false
    t.datetime "updated_at",    null: false
    t.string   "url_evenement"
    t.string   "url_ticket"
    t.string   "url_source"
  end

end
