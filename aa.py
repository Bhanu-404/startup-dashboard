"""
Module: Startup Analysis

This module provides an interactive web application for analyzing startup funding data.

Dependencies:
- streamlit (st)
- analysis (Investor,Overall,Startup)
- components (Investor,Overall,Startup)

Note: The `analysis` and `components` are imported from the `analysis` and `components` module.

Author: Abhishek Gupta
Github: https://github.com/1abhi6
"""

import streamlit as st

from analysis import (
    Investor as InvestorAnalysis,
    Overall as OverallAnalysis,
    Startup as StartupAnalysis
)

from components import (
    Investor as InvestorComponent,
    Overall as OverallComponent,
    Startup as StartupComponent
)

from components import PADDING_TOP


class Main:
    """
    Main class for the Startup Analysis application.

    Attributes:
        investor_analysis (InvestorAnalysis): An instance of the InvestorAnalysis class.
        investor_component (InvestorComponent): An instance of the InvestorComponent class.
        overall_analysis (OverallAnalysis): An instance of the OverallAnalysis class.
        overall_component (OverallComponent): An instance of the OverallComponent class.
        startup_analysis (StartupAnalysis): An instance of the StartupAnalysis class.
        startup_component (StartupComponent): An instance of the StartupComponent class.

    Methods:
        __init__: Initializes the Main class.
        home_component: Renders the home component based on the user's selection.
        investor: Renders the investor analysis component.
        overall: Renders the overall analysis component.
        startup: Renders the startup analysis component.
    """

    def __init__(self) -> None:
        """
        Initialize the Main class.
        """
        self.investor_analysis = InvestorAnalysis()
        self.investor_component = InvestorComponent()
        self.overall_analysis = OverallAnalysis()
        self.overall_component = OverallComponent()
        self.startup_analysis = StartupAnalysis()
        self.startup_component = StartupComponent()
        self.home_component()

    def home_component(self):
        """
        Render the home component based on the user's selection.
        """
        # Page configuration
        st.set_page_config(layout='wide', page_title="Abhi's Startup Analysis", page_icon='📊')
        st.sidebar.title(
            'Startup Funding analysis',
            help='Note: Data for Indian startups (2015-2020)'
        )
        option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'Startup', 'Investor'])

        if option == 'Overall Analysis':
            self.overall()
        elif option == 'Startup':
            self.startup()
        elif option == 'Investor':
            self.investor()

    def overall(self):
        """
        Render the overall analysis component.
        """

        # Give custom padding at top
        st.markdown(PADDING_TOP, unsafe_allow_html=True)

        # Make title center
        head_col_0, head_col_1, head_col_2 = st.columns(3)
        with head_col_0:
            st.write('')
        with head_col_1:
            st.header('Overall Analysis')
        with head_col_2:
            st.write('')
        st.divider()

        st.header('MoM Analysis', help='Analysis on the basis of month for quick overview.')
        st.divider()
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                'Total',
                str(self.overall_analysis.total_invested_amount()) + ' Cr',
                delta='50 Cr'
            )
        with col2:
            st.metric(
                'Maximum',
                str(self.overall_analysis.max_amount_infused()) + ' Cr'
            )

        with col3:
            st.metric(
                'Average',
                str(round(self.overall_analysis.avg_ticket_size())) + ' Cr',
                delta='20 Cr'
            )

        with col4:
            st.metric(
                'Total Funded Startups',
                self.overall_analysis.total_funded_startup(),
                delta='10'
            )

        st.divider()
        st.header(
            'MoM Graph',
            help='Graph on the basis of month for quick overview.'
        )
        st.divider()

        selected_option = st.selectbox(
            'Select Type of MoM chart',
            ['Total Amount of Funding MoM', 'Total Funded Indian Startups MoM']
        )

        st.divider()
        if selected_option == 'Total Amount of Funding MoM':
            self.overall_component.plot_total_funding_mom()
        else:
            self.overall_component.plot_total_funded_startup_mom()

        st.divider()
        self.overall_component.plot_most_funded_sector()

        st.divider()
        self.overall_component.plot_top_investors()

        st.divider()
        self.overall_component.plot_most_funded_startups_yoy()

        st.divider()
        self.overall_component.plot_most_funded_cities()

        st.divider()
        self.overall_component.plot_most_funded_type()

        st.divider()
        self.overall_component.plot_funding_amount_year_month()

    def startup(self):
        """
        Render the startup analysis component.
        """
        startup_name = st.sidebar.selectbox(
            'Select Startup',
            self.startup_analysis.list_of_startups()
        )
        btn = st.sidebar.button('Find Startup details')

        # Give custom padding at top
        st.markdown(PADDING_TOP, unsafe_allow_html=True)

        # Make title center
        head_col_0, head_col_1, head_col_2 = st.columns(3)
        with head_col_0:
            st.write('')
        with head_col_1:
            st.header('Startup Analysis')
        with head_col_2:
            st.write('')
        st.divider()

        if btn:
            subhead_col0, subhead_col1 = st.columns(2)

            with subhead_col0:
                st.subheader(startup_name + ' ' + 'Analysis',
                            help=f'Overall analysis of {startup_name}'
                )
            with subhead_col1:
                st.metric(
                    'Investments (In Crore Rs)',
                    self.startup_analysis.funding(startup_name),
                    delta='+10'
                )
            st.divider()

            col0, col1 = st.columns(2)
            with col0:
                st.metric('Sector', self.startup_analysis.sector(startup_name))
            with col1:
                st.metric('Subsector', self.startup_analysis.subsector(startup_name))

            st.divider()
            col3, col4 = st.columns(2)
            with col3:
                st.metric('Stage', self.startup_analysis.stage(startup_name))
            with col4:
                st.metric('Investors', self.startup_analysis.investors(startup_name))

            st.divider()
            self.startup_component.similar_startups(startup_name)


    def investor(self):
        """
        Render the investor analysis component.
        """
        # Get the investor name
        investor_name = st.sidebar.selectbox(
            'Select Investor',
            self.investor_analysis.investor_list()
        )

        btn = st.sidebar.button('Find Investor details')

        # Give custom padding at top
        st.markdown(PADDING_TOP, unsafe_allow_html=True)

        # Make title center
        head_col_0, head_col_1, head_col_2 = st.columns(3)
        with head_col_0:
            st.write('')
        with head_col_1:
            st.header('Investor Detail')
        with head_col_2:
            st.write('')
        st.divider()

        st.title(investor_name)
        st.divider()

        # Display the investor details
        if btn:
            self.investor_component.recent_five_investments(investor_name)
            st.divider()

            col1, col2 = st.columns(2)
            with col1:
                self.investor_component.plot_biggest_investment(investor_name)
            with col2:
                self.investor_component.plot_invested_city(investor_name)
            st.divider()

            col3, col4 = st.columns(2)
            with col3:
                self.investor_component.plot_invested_sector(investor_name)
            with col4:
                self.investor_component.plot_invested_subsector(investor_name)
            st.divider()

            col5, col6 = st.columns(2)
            with col5:
                self.investor_component.plot_invested_type(investor_name)
            with col6:
                self.investor_component.plot_yoy_investment(investor_name)
            st.divider()

            self.investor_component.similar_investors(investor_name)


Main()