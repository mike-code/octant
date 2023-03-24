// eslint-disable-next-line import/no-extraneous-dependencies
import 'regenerator-runtime/runtime';
import { ApolloProvider } from '@apollo/client';
import { Web3Modal } from '@web3modal/react';
import React from 'react';
import ReactDOM from 'react-dom/client';
import { QueryClientProvider } from 'react-query';
import { Provider } from 'react-redux';
import { HashRouter } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import { WagmiConfig } from 'wagmi';

import clientApollo from './api/clients/client-apollo';
import { ethereumClient } from './api/clients/client-ethereum';
import clientReactQuery from './api/clients/client-react-query';
import { wagmiClient } from './api/clients/client-wagmi';
import AppContainer from './App/AppContainer';
import { PROJECT_ID } from './constants/walletConnect';
import store from './store';

const root = document.getElementById('root')!;
ReactDOM.createRoot(root).render(
  <Provider store={store}>
    <WagmiConfig client={wagmiClient}>
      <ApolloProvider client={clientApollo}>
        <QueryClientProvider client={clientReactQuery}>
          <HashRouter>
            <AppContainer />
          </HashRouter>
          <ToastContainer
            position="top-center"
            style={{ overflowWrap: 'break-word', width: '350px' }}
            theme="dark"
          />
        </QueryClientProvider>
      </ApolloProvider>
    </WagmiConfig>
    <Web3Modal ethereumClient={ethereumClient} projectId={PROJECT_ID} />
  </Provider>,
);
