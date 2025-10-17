import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import FeatureCard from './FeatureCard.vue'

describe('FeatureCard', () => {
  it('renders properly with props', () => {
    const wrapper = mount(FeatureCard, {
      props: {
        icon: 'shield-check',
        title: 'Secure',
        description: 'Enterprise-grade security',
      },
    })

    expect(wrapper.find('h3').text()).toBe('Secure')
    expect(wrapper.find('p').text()).toBe('Enterprise-grade security')
  })

  it('displays the correct icon', () => {
    const wrapper = mount(FeatureCard, {
      props: {
        icon: 'lightning-bolt',
        title: 'Fast',
        description: 'Lightning fast performance',
      },
    })

    const icon = wrapper.find('[name="lightning-bolt"]')
    expect(icon.exists()).toBe(true)
  })
})

