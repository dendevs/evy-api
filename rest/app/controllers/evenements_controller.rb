class EvenementsController < ApplicationController
    skip_before_filter :verify_authenticity_token

    def index
        @evenements = Evenement.all
    end 

    def show
        @evenement = Evenement.find( params[:id] )
    end

    def new
        @evenement = Evenement.new
    end

    def edit
        @evenement = Evenement.find( params[:id] )
    end

    def create
        @evenement = Evenement.new( evenement_params )

        if @evenement.save
            redirect_to @evenement
        else
            render 'new'
        end
    end

    def update
        @evenement = Evenement.find( params[:id] )

        if @evenement.update( evenement_params )
            redirect_to @evenement
        else
            render 'edit'
        end
    end

    def destroy
        @evenement.finf( params[:id] )
        @evenement.destroy

        redirect_to evenements_path
    end

    private
    def evenement_params
        params.require(:evenement).permit( :title, :description )
    end

    # edit create update destroy
end
