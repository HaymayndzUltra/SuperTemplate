#!/usr/bin/env python3
"""
Real Live Monitoring Dashboard
Shows real-time validation metrics
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
import time
from datetime import datetime, timedelta
import requests

class RealMonitoringDashboard:
    def __init__(self):
        self.metrics_history = []
        self.api_endpoints = {
            'grammarly': 'https://api.grammarly.com/v1/check',
            'readability': 'https://readability-api.com/analyze',
            'compliance': 'https://compliance-checker.com/api/v1/analyze'
        }
    
    def get_real_time_metrics(self, text: str) -> Dict[str, Any]:
        """Get real-time metrics from external APIs"""
        metrics = {
            'timestamp': datetime.now().isoformat(),
            'text_length': len(text),
            'word_count': len(text.split()),
            'external_checks': {}
        }
        
        # Check external APIs
        for service, endpoint in self.api_endpoints.items():
            try:
                if service == 'grammarly':
                    response = requests.post(endpoint, json={'text': text})
                elif service == 'readability':
                    response = requests.get(endpoint, params={'text': text})
                elif service == 'compliance':
                    response = requests.post(endpoint, json={'text': text})
                
                if response.status_code == 200:
                    metrics['external_checks'][service] = response.json()
                else:
                    metrics['external_checks'][service] = {"error": f"HTTP {response.status_code}"}
                    
            except Exception as e:
                metrics['external_checks'][service] = {"error": str(e)}
        
        return metrics
    
    def create_dashboard(self):
        """Create real-time monitoring dashboard"""
        st.title("🔍 Real Proposal Validation Dashboard")
        
        # Sidebar for input
        st.sidebar.header("Input")
        proposal_text = st.sidebar.text_area("Enter proposal text:", height=200)
        
        if st.sidebar.button("Run Real Validation"):
            with st.spinner("Running real external validation..."):
                metrics = self.get_real_time_metrics(proposal_text)
                self.metrics_history.append(metrics)
                
                # Display results
                st.success("✅ Real validation complete!")
                
                # Metrics overview
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Text Length", metrics['text_length'])
                with col2:
                    st.metric("Word Count", metrics['word_count'])
                with col3:
                    st.metric("External Checks", len(metrics['external_checks']))
                
                # External API results
                st.subheader("🌐 External API Results")
                for service, result in metrics['external_checks'].items():
                    with st.expander(f"{service.title()} Results"):
                        if 'error' in result:
                            st.error(f"❌ {result['error']}")
                        else:
                            st.success("✅ API call successful")
                            st.json(result)
                
                # Real-time charts
                if len(self.metrics_history) > 1:
                    st.subheader("📊 Real-Time Metrics")
                    
                    # Create DataFrame for plotting
                    df = pd.DataFrame(self.metrics_history)
                    df['timestamp'] = pd.to_datetime(df['timestamp'])
                    
                    # Plot metrics over time
                    fig = px.line(df, x='timestamp', y='word_count', 
                                title='Word Count Over Time')
                    st.plotly_chart(fig)
        
        # Historical data
        if self.metrics_history:
            st.subheader("📈 Historical Data")
            df = pd.DataFrame(self.metrics_history)
            st.dataframe(df)
            
            # Export data
            if st.button("Export Data"):
                with open('real_validation_history.json', 'w') as f:
                    json.dump(self.metrics_history, f, indent=2)
                st.success("Data exported to real_validation_history.json")

if __name__ == "__main__":
    dashboard = RealMonitoringDashboard()
    dashboard.create_dashboard()
